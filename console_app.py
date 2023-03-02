import conv

def menu() -> None:
    while True:
        match input('> '):
            case 'get': 
                if conv.confirm_choice(): 
                    print(conv.get_update_data())
            case 'print': 
                for (el_key, value) in conv.current_session['quotes'].items(): print(f'{el_key[:3]} -> {el_key[3:]} >> {value}')
            case 'conv':
                print('>> Введите код операции!')
                choice = input('[conv]> ') # проверка наличия в списке, КОД - красивый вывод
                if conv.check_code(choice):
                    print('>> Введите значение!')
                    value = input('[conv]> ')
                    res = conv.convertation(choice, value)
                    print(f'{value} {choice[:3]} = ' + "%.3f" % res + f' {choice[3:]}')
                else: print('>> Введен неправильный код!')
            case 'help': pass # коды активации
            case 'exit': break
            case _: print('>> Неправильная команда!')

if __name__ == '__main__':
    # check for session and currencies
    conv.CURRENCIES = conv.fill_currencies()
    conv.set_session()
    menu()