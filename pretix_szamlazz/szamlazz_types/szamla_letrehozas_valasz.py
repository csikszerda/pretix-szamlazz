from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.szamlazz.hu/xmlszamlavalasz"


@dataclass(kw_only=True)
class Szamlavalasz:
    class Meta:
        name = "szamlavalasz"

    sikeres: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
            "required": True,
        }
    )
    hibakod: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    hibauzenet: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    szamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    szamlanetto: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    szamlabrutto: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    kintlevoseg: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    vevoifiokurl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
        },
    )
    pdf: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.szamlazz.hu/xmlszamlavalasz",
            "format": "base64",
        },
    )


@dataclass(kw_only=True)
class SzamlaValasz(Szamlavalasz):
    class Meta:
        name = "xmlszamlavalasz"
        namespace = "http://www.szamlazz.hu/xmlszamlavalasz"
