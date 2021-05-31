import json
from datetime import datetime
import sys
import os

import pandas as pd

from kafka_modules.consumer import Consume

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(ROOT_DIR)
NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks')
NOTEBOOKS_DATA_DIR = os.path.join(NOTEBOOKS_DIR, 'data')

consumer = Consume('customers_purchase').consumeData
items = []
for data in consumer:
    consumer_data = json.loads(data.value)
    df = pd.json_normalize(consumer_data)
    df.to_csv(f'{NOTEBOOKS_DATA_DIR}/my_csv.csv', mode='a', index=False)