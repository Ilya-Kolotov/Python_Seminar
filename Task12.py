# 12. Для натурального n создать словарь
#  индекс-значение, состоящий из элементов 
#  последовательности 3n + 1.    
#     *Пример:*    
#     - Для n = 6: {1: 4, 2: 7, 3: 
#     10, 4: 13, 5: 16, 6: 19}

N = int(input('Введите число N: '))
dictionary = {}
for i in range(1, N+1):
    dictionary[i] = i*3 + 1
print(dictionary)