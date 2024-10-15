from datetime import datetime
from decimal import Decimal
from typing import Sequence

class Country:
  name: str

class InvoiceAddress:
  name: str
  zipcode: str
  city: str
  street: str
  country: Country
  internal_reference: str
  vat_id: str
  company: str

class Event:
  name: str
  date_from: datetime

class Product:
  name: str

class OrderPosition:
  item: Product
  event: Event
  subevent: Event | None
  price: Decimal

class Positions:
  def all(self) -> Sequence[OrderPosition]: ...

class Order:
  code: str
  email: str
  phone: str
  invoice_address: InvoiceAddress
  positions: Positions