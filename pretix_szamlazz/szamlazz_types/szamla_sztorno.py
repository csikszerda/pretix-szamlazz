from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.szamlazz.hu/xmlszamlast"


@dataclass(kw_only=True)
class Beallitasok:
    class Meta:
        name = "beallitasokTipus"

    felhasznalo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    jelszo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    szamlaagentkulcs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    eszamla: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
            "required": True,
        }
    )
    szamla_letoltes: bool = field(
        metadata={
            "name": "szamlaLetoltes",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
            "required": True,
        }
    )
    szamla_letoltes_pld: Optional[int] = field(
        default=None,
        metadata={
            "name": "szamlaLetoltesPld",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    aggregator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    guardian: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    valasz_verzio: Optional[int] = field(
        default=None,
        metadata={
            "name": "valaszVerzio",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    szamla_kulso_azon: Optional[str] = field(
        default=None,
        metadata={
            "name": "szamlaKulsoAzon",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )


@dataclass(kw_only=True)
class Elado:
    class Meta:
        name = "eladoTipus"

    email_replyto: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailReplyto",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    email_targy: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailTargy",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    email_szoveg: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailSzoveg",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )


@dataclass(kw_only=True)
class Fejlec:
    class Meta:
        name = "fejlecTipus"

    szamlaszam: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
            "required": True,
        }
    )
    kelt_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "keltDatum",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    teljesites_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "teljesitesDatum",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    tipus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    szamla_sablon: Optional[str] = field(
        default=None,
        metadata={
            "name": "szamlaSablon",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )


@dataclass(kw_only=True)
class Vevo:
    class Meta:
        name = "vevoTipus"

    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    adoszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )
    adoszam_eu: Optional[str] = field(
        default=None,
        metadata={
            "name": "adoszamEU",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlast",
        },
    )


@dataclass(kw_only=True)
class SzamlaSztorno:
    class Meta:
        name = "xmlszamlast"
        namespace = "http://www.szamlazz.hu/xmlszamlast"

    beallitasok: Beallitasok = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    fejlec: Fejlec = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    elado: Optional[Elado] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vevo: Optional[Vevo] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
