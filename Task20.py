# Задайте список. Напишите программу, которая 
# определит, присутствует ли в заданном списке 
# строк некое число.

n = 5
a = ['123', '345', 123, '3567']
def isInt(a):
    for i in a:
        if type(i) == int:
            return True
    return False
print(isInt(a))