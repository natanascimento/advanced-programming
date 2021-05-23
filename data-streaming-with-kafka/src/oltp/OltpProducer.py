import os
import logging
import json

import dotenv

from kafka import KafkaProducer

class OltpProducer:
  
  def __init__(self, topic: str, data: dict):
    dotenv.load_dotenv(dotenv.find_dotenv())
    self.__topic = topic
    self.__data = json.dumps(data)
    self.__broker_server = '{}:{}'.format(os.getenv('KAFKA_SERVER'),
                                        os.getenv('KAFKA_PORT'))
    self.__producer = KafkaProducer(bootstrap_servers=self.__broker_server, 
                                  value_serializer=lambda v: str(v).encode('utf-8'))
    
  @property
  def produceData(self):
    try:
      return self.__producer.send(self.__topic, value=self.__data).get(timeout=60)
    except Exception as e:
      return e
  
  @property
  def getResults(self):
    return self.__producer