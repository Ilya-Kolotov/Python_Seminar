import validator

def show_answer(data):
    print(f'Ответ: {data}')

def view_data(data):
    print(data)

def get_value(text):
    result = input(text)
    while not validator.is_num(result):
        print('Нужно ввести число. Попробуйте снова: ')
        result = input()
    return int(result)

def get_complex_value(text):
    result = input(text)
    while not validator.is_complex(result):
        print('Нужно ввести комплексное число. Попробуйте снова: ')
        result = input()
    return complex(result)

def get_sign():
    signs = ['+', '-', '/', '*', '//', '%']
    sign = input('Введите знак операции (например, +): ')
    while sign not in signs:
        print('Такого знака нет. Введите корректный: ')
        sign = input()
    return sign

def get_sign_complex():
    signs = ['+', '-', '/', '*']
    sign = input('Введите знак операции (например, +): ')
    while sign not in signs:
        print('Такого знака нет. Введите корректный: ')
        sign = input()
    return sign

def get_mode():
    modes = ['1', '2']
    mode = input('Режимы:\n1 - работа с рациональными числами\n2 - работа с комлпексными числами\nВыбери: ')
    while mode not in modes:
        print('Такого режима нет. Введите корректный: ')
        mode = input()
    return mode