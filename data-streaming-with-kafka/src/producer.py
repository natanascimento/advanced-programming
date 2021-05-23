from oltp.OltpProducer import OltpProducer
from mock.customer import Customer

if __name__ == '__main__':
  while True:
    customer = Customer().generateCustomer
    producer = OltpProducer('customers_purchase', customer).produceData
    print (producer)