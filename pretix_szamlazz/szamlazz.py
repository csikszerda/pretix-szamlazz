from typing import TypeVar
import requests
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.parsers import XmlParser

from .szamlazz_types import *

xml_context = XmlContext()
xml_serializer = XmlSerializer(context=xml_context)
xml_parser = XmlParser(context=xml_context)

T = TypeVar("T")

def szamlazz_request(form_entry: str, request: object, response_type: type[T]) -> T:
  response = requests.post(url="https://www.szamlazz.hu/szamla/", files={
    form_entry: xml_serializer.render(request)
  })

  try:
    return xml_parser.from_string(response.text, response_type)
  except:
    raise RuntimeError(f"Could not parse response: " + response.text)

def szamla_letrehozas(szamla: SzamlaLetrehozas) -> SzamlaValasz:
  return szamlazz_request("action-xmlagentxmlfile", szamla, SzamlaValasz)

def szamla_sztorno(sztorno: SzamlaSztorno) -> SzamlaValasz:
  return szamlazz_request("action-szamla_agent_st", sztorno, SzamlaValasz)

def szamla_xml_lekeres(lekeres: SzamlaXmlLekeres) -> Szamla:
  return szamlazz_request("action-szamla_agent_xml", lekeres, Szamla) 