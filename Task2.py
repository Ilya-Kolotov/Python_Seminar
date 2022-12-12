# 2. Напишите программу, 
# которая на вход принимает 5 чисел и 
# находит максимальное из них.    
#     Примеры:    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
# num1 = InputNumbers('Введите число 1:')
# num2 = InputNumbers('Введите число 2:')
# num3 = InputNumbers('Введите число 3:')
# num4 = InputNumbers('Введите число 4:')
# num5 = InputNumbers('Введите число 5:')

# max = num1
# if num2 > max:
#     max = num2
# if num3 > max:
#     max = num3
# if num4 > max:
#     max = num4
# if num5 > max:
#     max = num5
# print(f'Введены числа {num1},{num2},{num3},{num4},{num5}')
# print(f'Максимальное число = {max}')

a = InputNumbers('Введите число: ')
maxx = a
for i in range(4):
    a = InputNumbers('Введите число: ')
    if a > maxx:
        maxx = a
print(f'Максимальное число = {maxx}')

