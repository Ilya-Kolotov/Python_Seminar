# 35. В файле находится N натуральных чисел, записанных
# через пробел. Среди чисел не хватает одного, чтобы
# выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

a_list = [1, 2, 3, 5, 6, 7, 8]

for i in range(len(a_list) - 1):
    if a_list[i+1] - a_list[i] > 1:
        print(a_list[i] + 1)