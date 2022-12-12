# 1. Напишите программу, которая принимает на вход 
# два числа и проверяет, 
# является ли одно число квадратом другого.    
#     *Примеры:*     
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
a = InputNumbers('Введите число А:')
b = InputNumbers('Введите число B:')
# numA = int(input('Введите чило А:'))
# numB = int(input('Введите число В:'))

# a = int(input('a = '))
# b = int(input('b = '))
if a == b ** 2 or b == a ** 2:
    print('Да')
else:
    print('Нет')

