# NOTE: This plugin is only set up to do the basic invoicing for Csíkszerda.
# If you use it, make sure you adjust it your needs!
# We take no responsibility for any problems if you use it.

from django.dispatch import receiver # pyright: ignore [ reportMissingTypeStubs, reportUnknownVariableType ]
from django.utils import translation # pyright: ignore [ reportMissingTypeStubs ]

from pretix.base.signals import order_paid, order_canceled
from pretix.base.models import Order
from xsdata.models.datatype import XmlDate
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.converter import Converter, converter
from i18nfield.fields import LazyI18nString
import datetime
import logging
from textwrap import dedent
import re
import zoneinfo
import os

import pretix_szamlazz.szamlazz_types.szamla_letrehozas as SzamlaLetrehozas
import pretix_szamlazz.szamlazz_types.szamla_sztorno as SzamlaSztorno
import pretix_szamlazz.szamlazz_types.szamla_xml_lekeres as SzamlaLekeres
import pretix_szamlazz.szamlazz as szamlazz

logger = logging.getLogger(__name__)

budapest_time = zoneinfo.ZoneInfo("Europe/Budapest")

xml_context = XmlContext()
xml_serializer = XmlSerializer(context=xml_context)
xml_parser = XmlParser(context=xml_context)

class LazyI18nStringConverter(Converter):
  def deserialize(self, value: str, **kwargs) -> LazyI18nString:
    raise RuntimeError("Unimplemented.")

  def serialize(self, value: LazyI18nString, **kwargs) -> str:
    return value.localize("hu")

converter.register_converter(LazyI18nString, LazyI18nStringConverter)

@receiver(order_paid, dispatch_uid="order_paid_szamlazz")
def order_paid_szamlazz(sender, order: Order, **kwargs): # pyright: ignore [ reportMissingParameterType, reportUnknownParameterType ]
  today = datetime.datetime.now(budapest_time)
  today_xml = XmlDate(year=today.year, month=today.month, day=today.day)

  invoice_address = order.invoice_address

  with translation.override('hu'):
    comment = "A számla kiegyenlítése megtörtént, pénzügyi rendezést nem igényel."

    if invoice_address.internal_reference:
      comment +=  f"\n\nVevő megjegyzése: {invoice_address.internal_reference}"

    szamla = SzamlaLetrehozas.SzamlaLetrehozas(
      beallitasok=SzamlaLetrehozas.Beallitasok(
        szamlaagentkulcs=os.environ["SZAMLA_AGENT_KEY"],
        eszamla=True,
        valasz_verzio=2, # XML response
        szamla_letoltes=False,
        szamla_kulso_azon=order.code,
      ),
      fejlec=SzamlaLetrehozas.Fejlec(
        teljesites_datum=today_xml,
        fizetesi_hatarido_datum=today_xml,
        fizmod="Bankkártya",
        penznem="HUF", # TODO: assert this
        szamla_nyelve=SzamlaLetrehozas.SzamlaNyelve.HU,
        fizetve=True,
        rendeles_szam=order.code,
        megjegyzes=comment,
      ),
      elado=SzamlaLetrehozas.Elado(
        email_szoveg=dedent('''\
          Kedves [vevőneve]!

          Köszönjük rendelésedet a Csíkszerda jegyboltjában!

          Itt tudod megtekinteni a számládat:
        '''),
        email_targy="Csíkszerda számla",
        email_replyto="csikszerda.kozonsegszervezes@gmail.com",
      ),
      vevo=SzamlaLetrehozas.Vevo(
        nev=invoice_address.company if invoice_address.company else invoice_address.name,
        alairo_neve=invoice_address.name if invoice_address.company else None,
        irsz=invoice_address.zipcode,
        telepules=invoice_address.city,
        cim=invoice_address.street,
        email=order.email,
        adoszam=invoice_address.custom_field if invoice_address.company else None,
        adoszam_eu=invoice_address.vat_id if invoice_address.company else None,
        orszag=invoice_address.country.name,
        telefonszam=str(order.phone),
        send_email=True,
      ),
      tetelek=SzamlaLetrehozas.Tetelek(tetel=[
        SzamlaLetrehozas.Tetel(
          megnevezes=position.item.name,
          megjegyzes=f"{(position.subevent or position.event).name} - {(position.subevent or position.event).date_from.astimezone(budapest_time).strftime('%Y. %m. %d. %H:%M')}",
          mennyiseg=1,
          mennyisegi_egyseg="db",
          netto_egysegar=float(position.price),
          afakulcs="AAM", # TODO: assert this
          netto_ertek=float(position.price),
          afa_ertek=0,
          brutto_ertek=float(position.price),
        )
        for position in order.positions.all()
      ])
    )

  szamlazz_response = szamlazz.szamla_letrehozas(szamla)

  if szamlazz_response.sikeres:
    logger.info(f"Sent szamlazz.hu invoice {szamlazz_response.szamlaszam} for order {order.code}")
  else:
    logger.error(f"Could not send szamlazz.hu invoice: {szamlazz_response}")

@receiver(order_canceled, dispatch_uid="order_canceled_szamlazz")
def order_canceled_szamlazz(sender, order: Order, **kwargs): # pyright: ignore [ reportMissingParameterType, reportUnknownParameterType ]
  try:
    order_invoice = szamlazz.szamla_xml_lekeres(SzamlaLekeres.SzamlaXmlLekeres(
      szamlaagentkulcs=os.environ["SZAMLA_AGENT_KEY"],
      rendeles_szam=order.code,
    ))
  except:
    raise RuntimeError(f"Could not get szamlazz.hu invoice for order code {order.code}")

  if order_invoice.alap.tipus == "SS":
    logger.warn(f"Szamlazz.hu invoice for order code {order.code} has already been cancelled by invoice {order_invoice.alap.szamlaszam}")
    return

  today = datetime.datetime.now(budapest_time)
  today_xml = XmlDate(year=today.year, month=today.month, day=today.day)

  sztorno_szamla = szamlazz.szamla_sztorno(SzamlaSztorno.SzamlaSztorno(
    beallitasok=SzamlaSztorno.Beallitasok(
      szamlaagentkulcs=os.environ["SZAMLA_AGENT_KEY"],
      eszamla=True,
      szamla_letoltes=False,
      valasz_verzio=2, # XML response
    ),
    fejlec=SzamlaSztorno.Fejlec(
      szamlaszam=order_invoice.alap.szamlaszam,
      kelt_datum=today_xml,
    ),
    elado=SzamlaSztorno.Elado(
      email_szoveg=dedent('''\
        Kedves [vevőneve]!

        Töröltük rendelésedet a Csíkszerda jegyboltjában!

        Itt tudod megtekinteni a sztornó számládat:
      '''),
      email_targy="Csíkszerda sztornó számla",
      email_replyto="csikszerda.kozonsegszervezes@gmail.com",
    ),
    vevo=SzamlaSztorno.Vevo(
      email=order_invoice.vevo.email,
    ),
  ))

  logger.info(f"Szamlazz.hu invoice {order_invoice.alap.szamlaszam} for order code {order.code} successfully cancelled by invoice {sztorno_szamla.szamlaszam}")