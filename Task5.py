# 3. Напишите программу, которая принимает на вход 
# число и проверяет, кратно ли оно 5 и 10 или 15, 
# но не 30.

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
num = InputNumbers('Введите число: ')

if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and  num % 30 !=0:
    print(True)
else:
    print(False)