# 1)Создайте список из случайных чисел. 
# Найдите максимальное количество его одинаковых 
# элементов.
# 1
import random
numbers = list()
for i in range(10):
    numbers.append(random.randint(2,5))
max_count = 0
for i in range(len(numbers)):
    count = 1    
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            count +=1
    if count > max_count:
        max_count = count

print(numbers)
print(max_count)

# 2
# import random

# max_count = 0
# numbers = list()
# for i in range(10):
#     numbers.append(random.randint(2,5))
# print(numbers)
# i=0
# while i<len(numbers)-max_count:
#     count = 1
#     for j in range(i+1,len(numbers)):
#         if numbers[i] == numbers[j]:
#             count += 1
    
#     if count > max_count:
#         max_count = count
#     i+=1
# print(max_count)


# import random

# a = 1
# b = 6

# array = [random.randint(a, b) for i in range(20)]
# print(array)

# d = {}

# for i in array:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
    
# print(d)

# max = 0
# for i in range(a, (b+1)):
#     if(d[i] > max):
#         max = d[i]

# print(f"Максимальное повторение элемента {max} раз.")

# import random

# list_num = []
# max = 0
# for i in range(10):
#     a= random.randint(2,5)
#     list_num.append(a)
# print(list_num)
# print(set(list_num))
# for i in set(list_num):
#     if list_num.count(i)>max:
#         max = list_num.count(i)
# print(max)
