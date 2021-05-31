from pydantic import BaseModel

class Product(BaseModel):
  nome: str
  categoria: str