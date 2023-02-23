import requests
import os

headers = {}

with open(f"{os.path.dirname(os.path.abspath(__file__))}/setup/api_key.txt") as key_holder:
    headers['apikey'] = key_holder.read()
    key_holder.close()

data = requests.get('https://api.apilayer.com/currency_data/live?', headers=headers)

print(data.text)