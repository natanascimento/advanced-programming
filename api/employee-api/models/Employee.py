from datetime import datetime

from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional

class EmployeeModel(BaseModel):
    matricula: str = Field(...)
    nome: str = Field(...)
    email: EmailStr = Field(...)
    dataDeCadastro: str = Field(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "matricula": "1181177100",
                "nome": "natan Nascimento",
                "email": "natan.oliveira@souunit.com.br",
            }
        }

class UpdateEmployeeModel(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "nome": "natan Nascimento",
                "email": "natan.oliveira@souunit.com.br",
            }
        }