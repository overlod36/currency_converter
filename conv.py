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
    if not check_float(value): print('>> Введено не число!')
    else:
        to_conv = float(value)
        if choice[:3] == 'USD': return float(current_session['quotes'][choice]) * to_conv
        elif choice[3:] == 'USD': return to_conv / float(current_session['quotes'][choice[3:] + choice[:3]])
        else: return to_conv * (1 / current_session['quotes']['USD' + choice[:3]]) * current_session['quotes']['USD' + choice[3:]]

def confirm_choice() -> bool:
    while True:
        print('>> Вы действительно хотите совершить это действие?[Да(1)/Нет(0)]')
        answer = input('[confirm]> ')
        if answer not in ('0', '1'): print('>> Неправильный ввод!')
        else:
            if answer == '0': return False
            else: return True

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

def set_session() -> None:
    global current_session
    if len(os.listdir(f'{PATH}\journals')) != 0: current_session = get_session(list(reversed(os.listdir(f'{PATH}\journals')))[0])
 
def get_api_key() -> None:
    with open(f"{PATH}/setup/api_key.txt") as key_holder:
        headers['apikey'] = key_holder.read()
        key_holder.close()

def get_update_data() -> str:
    if len(headers) == 0: get_api_key()
    try: save_new_session(requests.get('https://api.apilayer.com/currency_data/live?', headers=headers).json())
    except requests.exceptions.Timeout:
        return 'Ошибка: Timeout'
    except requests.exceptions.ConnectionError:
        return 'Ошибка: ConnectionError'
    return ''



def get_currency_index(currency: str) -> int:
    if not currency in CURRENCIES: return 0
    else: return list(CURRENCIES.keys()).index(currency)