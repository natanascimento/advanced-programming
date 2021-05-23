from datetime import datetime
from uuid import uuid5, NAMESPACE_DNS

from faker import Faker

class Customer:

  def __init__(self):
    self.__fake = Faker()
    self.__customer_id = str(uuid5(NAMESPACE_DNS, 'unit.br'))
    self.__customer_name = self.__fake.name()
    self.__customer_address = self.__fake.address().replace('\n', ' - ')
    self.__customer_buy_price = self.__fake.pricetag()
    self.__createdAt = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
  
  @property
  def generateCustomer(self):
    customer = {"customer_id": self.__customer_id,
                "customer_name": self.__customer_name,
                "customer_address": self.__customer_address,
                "customer_purchase_price": self.__customer_buy_price,
                "createdAt": self.__createdAt}
    
    return customer