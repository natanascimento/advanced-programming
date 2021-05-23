import os

import dotenv

from kafka import KafkaConsumer

class Consume: 

    def __init__(self, topic: str):
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.__topic = topic
        self.__broker_server = '{}:{}'.format(os.getenv('KAFKA_SERVER'),
                                        os.getenv('KAFKA_PORT'))
        
    @property
    def consumeData(self):
        try:
            consumer = KafkaConsumer(self.__topic, 
                                    bootstrap_servers=self.__broker_server)
            return consumer
        except Exception as e:
            return e