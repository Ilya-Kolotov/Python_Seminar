# 43)Имеется список id сотрудников из 10 элементов, каждый id -
# случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)
# Сопоставьте каждому имени сотрудника его id по порядку, и выведите
# получившийся список кортежей.
# Отсортировать список по возрастанию id.
# Выведете имена сотрудников, получившие нечетное id.
# Решить с помощью zip,filter,lambda
import random

id_sotr = random.sample(range(0, 101), 10)
print(id_sotr)
name_sotr = ["Илья1","Илья2","Илья3","Илья4","Илья5","Илья6","Илья7","Илья8","Илья9","Илья10",]

res = list(zip(id_sotr, name_sotr))
print(res)

# res = sorted(res, key = lambda x: x[0])
# print(res)
res = list(filter(lambda x: x[0] % 2, sorted(res)))
print(res)
names_list = list(map(lambda x : x[1], res))
print(names_list)