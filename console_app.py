import conv
import sys

def check_float(num: str) -> bool:
    try: float(num)
    except ValueError: return False
    else: return True

def confirm_choice() -> bool:
    while True:
        print('>> Вы действительно хотите совершить это действие?[Да(1)/Нет(0)]')
        answer = input('[confirm]> ')
        if answer not in ('0', '1'): print('>> Неправильный ввод!')
        else:
            if answer == '0': return False
            else: return True

def menu() -> None:
    while True:
        match input('> '):
            case 'get': 
                if confirm_choice(): 
                    print(conv.get_update_data())
            case 'print': 
                for (el_key, value) in conv.current_session['quotes'].items(): print(f'{el_key[:3]} -> {el_key[3:]} >> {value}')
            case 'conv':
                print('>> Введите код операции!')
                choice = input('[conv]> ') # проверка наличия в списке, КОД - красивый вывод
                if conv.check_code(choice):
                    print('>> Введите значение!')
                    value = input('[conv]> ')
                    if not check_float(value): print('>> Введено не число!')
                    else: 
                        res = conv.convertation(choice, value)
                        print(f'{value} {choice[:3]} = ' + "%.3f" % res + f' {choice[3:]}')
                else: print('>> Введен неправильный код!')
            case 'help': pass # коды активации
            case 'exit': break
            case _: print('>> Неправильная команда!')

if __name__ == '__main__':
    # check for session and currencies
    conv.CURRENCIES = conv.fill_currencies()
    if not conv.set_session():
        ms = conv.get_update_data()
        if ms != '': 
            print(f'Не удалось загрузить сессию => [{ms}]')
            wait = input()
            sys.exit()
    menu()