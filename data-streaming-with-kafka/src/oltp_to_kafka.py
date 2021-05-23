from data.producer import Produce
from mock.customer import Customer
from mock.stocks import Ticket

if __name__ == '__main__':
  while True:
    customer = Customer().generateCustomer
    #ticket = Ticket('XAU').getTicketPrice
    customer_producer = Produce('customers_purchase', customer).produceData
    #ticket_producer = OltpProducer('tickets_price', ticket).produceData
    #print(f'Customer: {customer_producer}\nTicket: {ticket_producer}')
    print(f'Customer: {customer_producer}')