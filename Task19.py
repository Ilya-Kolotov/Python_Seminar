# Реализуйте алгоритм задания случайных чисел без 
# использования встроенного генератора 
# псевдослучайных чисел.
import datetime
def random_num(n):
    randomNum = datetime.datetime.now().microsecond
    return randomNum % n+1

n = int(input('Введите число: '))
print(random_num(n))
list_num =[]
for i in range(n):
    a = random_num(n)
    list_num.append(a)
print(list_num)