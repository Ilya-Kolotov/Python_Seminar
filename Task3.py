# 3. Напишите программу, которая будет на вход 
# принимать число N и выводить числа от -N до N    
#     *Примеры:*     
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 

def InputNumbers(InputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f'{InputText}'))
            is_OK = True
        except ValueError:
            print('Ошибка! Введите число')
    return number
numN = InputNumbers('Введите число N:')
if numN > 0:
    numbers = list(range(-numN, numN+1))
else:
    numbers = list(range(numN,-numN+1))
print(numbers)

