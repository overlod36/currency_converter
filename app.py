import requests
import os
from datetime import datetime
import json

PATH = os.path.dirname(os.path.abspath(__file__))

headers = {}
current_session = {}

def convertation(choice: int) -> None:
    patterns = ['USDRUB', 'USDEUR', 'RUBUSD', 'RUBEUR', 'EURUSD', 'EURRUB']
    print('>> Введите значение!')
    value = input('[conv]> ')
    if not value.replace('.', '', 1): print('>> Введено не число!')
    else:
        to_conv = float(value)
        if patterns[choice][:3] == 'USD':
            res = float(current_session['quotes'][patterns[choice]]) * to_conv
            print(f'{value} {patterns[choice][:3]} = ' + "%.3f" % res + f' {patterns[choice][3:]}')
        else:
            print('>> В процессе!')

def confirm_choice() -> bool:
    while True:
        print('>> Вы действительно хотите совершить это действие?[Да(1)/Нет(0)]')
        answer = input('[confirm]> ')
        if answer not in ('0', '1'): print('>> Неправильный ввод!')
        else:
            if answer == '0': return False
            else: return True

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

def get_update_data() -> None:
    if len(headers) == 0: get_api_key()
    save_new_session(requests.get('https://api.apilayer.com/currency_data/live?', headers=headers).json())

def menu() -> None:
    while True:
        match input('> '):
            case 'get': 
                if confirm_choice(): get_update_data()
            case 'print': 
                for (el_key, value) in current_session['quotes'].items(): print(f'{el_key[:3]} -> {el_key[3:]} >> {value}')
            case 'conv': 
                print('>> [1] USD -> RUB [2] USD -> EUR [3] RUB -> USD [4] RUB -> EUR [5] EUR -> USD [6] EUR -> RUB')
                choice = input('[conv]> ')
                if not choice.isnumeric(): print('>> Введено не число!')
                else:
                    if not 1 <= int(choice) <= 6: print('>> Неправильный ввод!')
                    else: convertation(int(choice) - 1)
            case 'help': pass 
            case 'exit': break
            case _: print('>> Неправильная команда!')

if __name__ == '__main__':
    set_session()
    menu()