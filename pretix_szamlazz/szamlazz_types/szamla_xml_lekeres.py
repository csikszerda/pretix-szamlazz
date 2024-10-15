from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.szamlazz.hu/xmlszamlaxml"


@dataclass(kw_only=True)
class SzamlaXmlLekeres:
    class Meta:
        name = "xmlszamlaxml"
        namespace = "http://www.szamlazz.hu/xmlszamlaxml"

    felhasznalo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    jelszo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    szamlaagentkulcs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    szamlaszam: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rendeles_szam: Optional[str] = field(
        default=None,
        metadata={
            "name": "rendelesSzam",
            "type": "Element",
        },
    )
    pdf: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
