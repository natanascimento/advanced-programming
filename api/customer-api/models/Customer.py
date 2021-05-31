from pydantic import BaseModel

class Customer(BaseModel):
  nome: str
  email: str