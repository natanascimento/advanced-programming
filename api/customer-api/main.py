from datetime import datetime
import os
from uuid import uuid5, NAMESPACE_DNS

import dotenv
from fastapi import FastAPI, Response, HTTPException

from models.Customer import Customer
from models.Product import Product

app = FastAPI()
dotenv.load_dotenv(dotenv.find_dotenv())

#Customer
@app.get('/v1/customer', status_code=200)
async def getCustomer(customer_id: str):
  return {"customer_id": customer_id}

@app.post('/v1/customer', status_code=201)
async def customerSignUp(customer: Customer):
  return {"id": uuid5(NAMESPACE_DNS, 'natanascimento.com'), "nome":customer.nome, "email": customer.email, "signupDate": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}

#Product
@app.get('/v1/product', status_code=200)
async def getProduct(product_id: str):
  return {"product_id": product_id}

@app.post('/v1/product', status_code=201)
async def productRegister(product: Product):
  return {"id": uuid5(NAMESPACE_DNS, 'natanascimento.com'), "nome":product.nome, "categoria":product.categoria, "createdAt": datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}

@app.get('/v1/validation')
async def studentValidator(user: str, password: str, response: Response):
  if user == os.getenv('USERNAME_TEST') and password == os.getenv('PASSWORD_TEST'):
    response.status_code = 200
    return {"info": "It's pretty good to see you again!", "Authorization": True}
  else:
    raise HTTPException(
      status_code=401, detail=f"You don't have permission to use this! Permission Status: {False}"
    )