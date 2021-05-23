import json
import requests as r

class Ticket:

    def __init__(self, ticket: str):
        self.ticket = ticket
        self.url = f'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/{self.ticket}/USD'
        
    @property
    def getTicketPrice(self):
        response = r.get(self.url)
        ticket_data = json.loads(response.text)

        return ticket_data