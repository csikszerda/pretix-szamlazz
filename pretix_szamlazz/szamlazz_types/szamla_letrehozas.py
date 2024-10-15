from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.szamlazz.hu/xmlszamla"


@dataclass(kw_only=True)
class Beallitasok:
    class Meta:
        name = "beallitasokTipus"

    felhasznalo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    jelszo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    szamlaagentkulcs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    eszamla: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    szamla_letoltes: bool = field(
        metadata={
            "name": "szamlaLetoltes",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    szamla_letoltes_pld: Optional[int] = field(
        default=None,
        metadata={
            "name": "szamlaLetoltesPld",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    valasz_verzio: Optional[int] = field(
        default=None,
        metadata={
            "name": "valaszVerzio",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    aggregator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    guardian: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    cikkazoninvoice: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    szamla_kulso_azon: Optional[str] = field(
        default=None,
        metadata={
            "name": "szamlaKulsoAzon",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Elado:
    class Meta:
        name = "eladoTipus"

    bank: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    bankszamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    email_replyto: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailReplyto",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    email_targy: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailTargy",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    email_szoveg: Optional[str] = field(
        default=None,
        metadata={
            "name": "emailSzoveg",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    alairo_neve: Optional[str] = field(
        default=None,
        metadata={
            "name": "alairoNeve",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Mpl:
    class Meta:
        name = "mplTipus"

    vevokod: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    vonalkod: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    tomeg: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    kulonszolgaltatasok: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    erteknyilvanitas: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Ppp:
    class Meta:
        name = "pppTipus"

    vonalkod_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "vonalkodPrefix",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vonalkod_postfix: Optional[str] = field(
        default=None,
        metadata={
            "name": "vonalkodPostfix",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Sprinter:
    class Meta:
        name = "sprinterTipus"

    azonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    feladokod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    iranykod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    csomagszam: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vonalkod_postfix: Optional[str] = field(
        default=None,
        metadata={
            "name": "vonalkodPostfix",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    szallitasi_ido: Optional[str] = field(
        default=None,
        metadata={
            "name": "szallitasiIdo",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


class SzamlaNyelve(Enum):
    HU = "hu"
    EN = "en"
    DE = "de"
    IT = "it"
    RO = "ro"
    SK = "sk"
    HR = "hr"
    FR = "fr"
    ES = "es"
    CZ = "cz"
    PL = "pl"
    BG = "bg"
    NL = "nl"
    RU = "ru"
    SI = "si"


@dataclass(kw_only=True)
class TetelFokonyv:
    class Meta:
        name = "tetelFokonyvTipus"

    gazdasagi_esem: Optional[str] = field(
        default=None,
        metadata={
            "name": "gazdasagiEsem",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    gazdasagi_esem_afa: Optional[str] = field(
        default=None,
        metadata={
            "name": "gazdasagiEsemAfa",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    arbevetel_fokonyvi_szam: Optional[str] = field(
        default=None,
        metadata={
            "name": "arbevetelFokonyviSzam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    afa_fokonyvi_szam: Optional[str] = field(
        default=None,
        metadata={
            "name": "afaFokonyviSzam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    elsz_datum_tol: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "elszDatumTol",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    elsz_datum_ig: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "elszDatumIg",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Transoflex:
    class Meta:
        name = "transoflexTipus"

    azonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    shipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipmentID",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    csomagszam: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    zip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    service: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class VevoFokonyv:
    class Meta:
        name = "vevoFokonyvTipus"

    konyveles_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "konyvelesDatum",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vevo_azonosito: Optional[str] = field(
        default=None,
        metadata={
            "name": "vevoAzonosito",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vevo_fokonyvi_szam: Optional[str] = field(
        default=None,
        metadata={
            "name": "vevoFokonyviSzam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    folyamatos_telj: Optional[bool] = field(
        default=None,
        metadata={
            "name": "folyamatosTelj",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    elsz_datum_tol: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "elszDatumTol",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    elsz_datum_ig: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "elszDatumIg",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Fejlec:
    class Meta:
        name = "fejlecTipus"

    kelt_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "keltDatum",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    teljesites_datum: XmlDate = field(
        metadata={
            "name": "teljesitesDatum",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    fizetesi_hatarido_datum: XmlDate = field(
        metadata={
            "name": "fizetesiHataridoDatum",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    fizmod: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    penznem: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    szamla_nyelve: SzamlaNyelve = field(
        metadata={
            "name": "szamlaNyelve",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    arfolyam_bank: Optional[str] = field(
        default=None,
        metadata={
            "name": "arfolyamBank",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    arfolyam: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    rendeles_szam: Optional[str] = field(
        default=None,
        metadata={
            "name": "rendelesSzam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    dijbekero_szamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "name": "dijbekeroSzamlaszam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    elolegszamla: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vegszamla: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    eloleg_szamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "name": "elolegSzamlaszam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    helyesbitoszamla: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    helyesbitett_szamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "name": "helyesbitettSzamlaszam",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    dijbekero: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    szallitolevel: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    logo_extra: Optional[str] = field(
        default=None,
        metadata={
            "name": "logoExtra",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    szamlaszam_elotag: Optional[str] = field(
        default=None,
        metadata={
            "name": "szamlaszamElotag",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    fizetendo_korrekcio: Optional[float] = field(
        default=None,
        metadata={
            "name": "fizetendoKorrekcio",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    fizetve: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    arres_afa: Optional[bool] = field(
        default=None,
        metadata={
            "name": "arresAfa",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    eus_afa: Optional[bool] = field(
        default=None,
        metadata={
            "name": "eusAfa",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    szamla_sablon: Optional[str] = field(
        default=None,
        metadata={
            "name": "szamlaSablon",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    elonezetpdf: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Fuvarlevel:
    class Meta:
        name = "fuvarlevelTipus"

    uticel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    futar_szolgalat: Optional[str] = field(
        default=None,
        metadata={
            "name": "futarSzolgalat",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vonalkod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    tof: Optional[Transoflex] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    ppp: Optional[Ppp] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    sprinter: Optional[Sprinter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    mpl: Optional[Mpl] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Tetel:
    class Meta:
        name = "tetelTipus"

    megnevezes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    azonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    mennyiseg: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    mennyisegi_egyseg: str = field(
        metadata={
            "name": "mennyisegiEgyseg",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    netto_egysegar: float = field(
        metadata={
            "name": "nettoEgysegar",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    afakulcs: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    arres_afa_alap: Optional[float] = field(
        default=None,
        metadata={
            "name": "arresAfaAlap",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    netto_ertek: float = field(
        metadata={
            "name": "nettoErtek",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    afa_ertek: float = field(
        metadata={
            "name": "afaErtek",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    brutto_ertek: float = field(
        metadata={
            "name": "bruttoErtek",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    tetel_fokonyv: Optional[TetelFokonyv] = field(
        default=None,
        metadata={
            "name": "tetelFokonyv",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Vevo:
    class Meta:
        name = "vevoTipus"

    nev: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    orszag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    irsz: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    telepules: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    cim: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    send_email: Optional[bool] = field(
        default=None,
        metadata={
            "name": "sendEmail",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    adoalany: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    adoszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    csoportazonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    adoszam_eu: Optional[str] = field(
        default=None,
        metadata={
            "name": "adoszamEU",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    postazasi_nev: Optional[str] = field(
        default=None,
        metadata={
            "name": "postazasiNev",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    postazasi_orszag: Optional[str] = field(
        default=None,
        metadata={
            "name": "postazasiOrszag",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    postazasi_irsz: Optional[str] = field(
        default=None,
        metadata={
            "name": "postazasiIrsz",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    postazasi_telepules: Optional[str] = field(
        default=None,
        metadata={
            "name": "postazasiTelepules",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    postazasi_cim: Optional[str] = field(
        default=None,
        metadata={
            "name": "postazasiCim",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    vevo_fokonyv: Optional[VevoFokonyv] = field(
        default=None,
        metadata={
            "name": "vevoFokonyv",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    azonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    alairo_neve: Optional[str] = field(
        default=None,
        metadata={
            "name": "alairoNeve",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    telefonszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
        },
    )


@dataclass(kw_only=True)
class Tetelek:
    class Meta:
        name = "tetelekTipus"

    tetel: List[Tetel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamla",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SzamlaLetrehozas:
    class Meta:
        name = "xmlszamla"
        namespace = "http://www.szamlazz.hu/xmlszamla"

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
    elado: Elado = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    vevo: Vevo = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    fuvarlevel: Optional[Fuvarlevel] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tetelek: Tetelek = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
