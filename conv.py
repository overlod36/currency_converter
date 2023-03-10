import requests
import os
from datetime import datetime
import json

PATH = os.path.dirname(os.path.abspath(__file__))
CURRENCIES = {}

headers = {}
current_session = {}

def check_float(num: str) -> bool:
    try: float(num)
    except ValueError: return False
    else: return True

def convertation(choice: str, value: str) -> float:
    to_conv = float(value)
    if choice[:3] == 'USD': return float(current_session['quotes'][choice]) * to_conv
    elif choice[3:] == 'USD': return to_conv / float(current_session['quotes'][choice[3:] + choice[:3]])
    else: return to_conv * (1 / current_session['quotes']['USD' + choice[:3]]) * current_session['quotes']['USD' + choice[3:]]

def fill_currencies() -> dict:
    with open(f'{PATH}/setup/currencies.json', 'r', encoding='utf-8') as currencies:
        return json.load(currencies)

def check_code(code: str) -> bool:
    if len(code) != 6: return False
    if code[:3] in CURRENCIES.keys() and code[3:] in CURRENCIES.keys(): return True
    return False

def get_session(name: str) -> dict:
    with open(f'{PATH}/journals/{name}', 'r') as session:
        return json.load(session)
    
def save_new_session(data: dict) -> None:
    global current_session
    # check data
    with open(f'{PATH}/journals/{datetime.now().strftime("%d-%m-%Y(%H%M%S)")}.json', 'w', encoding='utf-8') as outf:
        json.dump(data, outf, ensure_ascii=False, indent=4)
        outf.close()
    current_session = data

def set_session() -> bool:
    global current_session
    if len(os.listdir(f'{PATH}\journals')) != 0: 
        current_session = get_session(list(reversed(os.listdir(f'{PATH}\journals')))[0])
        return True
    return False
 
def get_api_key() -> None:
    with open(f"{PATH}/setup/api_key.txt") as key_holder:
        headers['apikey'] = key_holder.read()
        key_holder.close()

def get_update_data() -> str:
    if len(headers) == 0: get_api_key()
    try: save_new_session(requests.get('https://api.apilayer.com/currency_data/live?', headers=headers, timeout=1).json())
    except requests.exceptions.Timeout:
        return '????????????: Timeout'
    except requests.exceptions.ConnectionError:
        return '????????????: ConnectionError'
    return ''

def get_currency_index(currency: str) -> int:
    if not currency in CURRENCIES: return 0
    else: return list(CURRENCIES.keys()).index(currency)