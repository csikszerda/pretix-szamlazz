from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.szamlazz.hu/szamla"


class Afatipus(Enum):
    TAM = "TAM"
    AAM = "AAM"
    EU = "EU"
    EUK = "EUK"
    MAA = "MAA"
    F_AFA = "F.AFA"
    K_AFA = "K.AFA"
    KK = "ÁKK"
    TAHK = "TAHK"
    TEHK = "TEHK"
    EUT = "EUT"
    EUKT = "EUKT"
    HO = "HO"
    EUE = "EUE"
    EUFADE = "EUFADE"
    EUFAD37 = "EUFAD37"
    ATK = "ATK"
    NAM = "NAM"
    EAM = "EAM"
    KBAUK = "KBAUK"
    KBAET = "KBAET"


@dataclass(kw_only=True)
class Bank:
    class Meta:
        name = "bankTipus"

    nev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    bankszamla: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Cim:
    class Meta:
        name = "cimTipus"

    orszag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    irsz: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    telepules: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    cim: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Cimkek:
    class Meta:
        name = "cimkekTipus"

    cimke: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Cimposta:
    class Meta:
        name = "cimpostaTipus"

    nev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    orszag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    irsz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    telepules: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    cim: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


class Fizmodunified(Enum):
    TUTAL_S = "átutalás"
    K_SZP_NZ = "készpénz"
    BANKK_RTYA = "bankkártya"
    CSEKK = "csekk"
    UT_NV_T = "utánvét"
    AJ_ND_KUTALV_NY = "ajándékutalvány"
    BARION = "barion"
    BARTER = "barter"
    CSOPORTOS_BESZED_S = "csoportos beszedés"
    OTP_SIMPLE = "OTP Simple"
    KOMPENZ_CI = "kompenzáció"
    KUPON = "kupon"
    PAY_PAL = "PayPal"
    PAY_U = "PayU"
    SZ_P_K_RTYA = "SZÉP kártya"
    UTALV_NY = "utalvány"
    EGY_B = "egyéb"


@dataclass(kw_only=True)
class Fokonyvtetel:
    class Meta:
        name = "fokonyvtetelTipus"

    arbevetel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    gazdasagiesemeny: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    gazdasagiesemenyafa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    elszdattol: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    elszdatig: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Fokonyvvevo:
    class Meta:
        name = "fokonyvvevoTipus"

    vevo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    vevoazon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    folyamatostelj: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    elsz_dat_tol: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "elszDatTol",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    elsz_dat_ig: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "elszDatIg",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Kifizetes:
    class Meta:
        name = "kifizetesTipus"

    datum: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    jogcim: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    osszeg: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    bankszamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    banktranzid: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    devizaarf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


class Nyelv(Enum):
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
class Totalossz:
    class Meta:
        name = "totalosszTipus"

    netto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    afa: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    brutto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Afakulcsossz:
    class Meta:
        name = "afakulcsosszTipus"

    afatipus: Optional[Afatipus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afakulcs: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    netto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    afa: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    brutto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Alap:
    class Meta:
        name = "alapTipus"

    id: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    szamlaszam: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    gazd_esem_azon: int = field(
        metadata={
            "name": "gazdEsemAzon",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    forras: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    iktatoszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    tipus: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    eszamla: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    hivszamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    hivdijbekszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    kelt: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    telj: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    fizh: XmlDate = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    fizmod: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    fizmodunified: Fizmodunified = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    keszpenz: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    rendelesszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    nyelv: Nyelv = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    devizanem: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    devizabank: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    devizaarf: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afatipus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    penzforg: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    kata: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    katafokonyv: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    teszt: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    sztornozott: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Kifizetesek:
    class Meta:
        name = "kifizetesekTipus"

    kifizetes: List[Kifizetes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Qutet:
    class Meta:
        name = "qutetTipus"

    nev: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    afatipus: Optional[Afatipus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afakulcs: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    netto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    afa: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    brutto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    elszdattol: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    elszdatig: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afalevon: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    cimkek: Optional[Cimkek] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Szallito:
    class Meta:
        name = "szallitoTipus"

    id: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    nev: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    cim: Cim = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    postacim: Optional[Cim] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    adoszam: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    csoportazonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    adoszameu: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    bank: Optional[Bank] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Tetel:
    class Meta:
        name = "tetelTipus"

    nev: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    azonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    mennyiseg: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    mennyisegiegyseg: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    nettoegysegar: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    afatipus: Optional[Afatipus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afakulcs: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    netto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    arresafaalap: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    afa: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    brutto: float = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    megjegyzes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    sztetordering: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    fokonyv: Optional[Fokonyvtetel] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Vevo:
    class Meta:
        name = "vevoTipus"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    nev: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    azonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    cim: Cim = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    postacim: Optional[Cimposta] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    adoszam: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    csoportazonosito: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    adoszameu: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )
    lokacio: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    private_person_indicator: bool = field(
        metadata={
            "name": "privatePersonIndicator",
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )
    fokonyv: Optional[Fokonyvvevo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
        },
    )


@dataclass(kw_only=True)
class Osszegek:
    class Meta:
        name = "osszegekTipus"

    afakulcsossz: List[Afakulcsossz] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "min_occurs": 1,
        },
    )
    totalossz: Totalossz = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Qutetek:
    class Meta:
        name = "qutetekTipus"

    qutet: List[Qutet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/szamla",
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
            "namespace": "http://www.szamlazz.hu/szamla",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Szamla:
    class Meta:
        name = "szamla"
        namespace = "http://www.szamlazz.hu/szamla"

    szallito: Szallito = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    alap: Alap = field(
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
    tetelek: Tetelek = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    qutetek: Optional[Qutetek] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cimkek: Optional[Cimkek] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    osszegek: Osszegek = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    kifizetesek: Optional[Kifizetesek] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pdf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
