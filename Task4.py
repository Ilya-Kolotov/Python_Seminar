# 2. Напишите программу, которая будет принимать 
# на вход дробь и показывать первую цифру 
# дробной части числа.    
#     *Примеры:*    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number

num = InputNumbers('Введите число: ')
if  num * 10 % 10 == 0: 
    print('нет')
else:
    print(int(num * 10 % 10))

# n = input()
# a=n.split(".")
# print(a[1][0])
