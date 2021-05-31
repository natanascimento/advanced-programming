from kafka_modules.producer import Produce
from mock.customer import Customer
from mock.stocks import Ticket

if __name__ == '__main__':
  while True:
    customer = Customer().generateCustomer
    customer_producer = Produce('customers_purchase', customer).produceData
    print(f'Customer: {customer_producer}')