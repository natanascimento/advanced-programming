import json
from datetime import datetime
import sys
import os

sys.path.append(os.getenv('MODULE_PATH'))

from data.consumer import Consume

consumer = Consume('customers_purchase').consumeData
items = []
for data in consumer:
    consumer_data = json.loads(data.value)
    print(consumer_data)