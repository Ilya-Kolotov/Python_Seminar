# 13. Напишите программу, в которой пользователь 
# будет задавать две строки, 
# а программа - определять количество
#  вхождений одной строки в другой.

stroka = input('Введите основную строку: ')
podstroka = input('Введите искомую подстроку: ')
count = 0
i=0
while i <= len(stroka)-len(podstroka): 
    vhodit = True
    for j in range(len(podstroka)):
        print(stroka[i+j])
        if stroka[i+j] != podstroka[j]:           
            vhodit = False
    if vhodit:
         count += 1 
         i=i+len(podstroka)
    else:   
       i = i + 1    
print(count)

# препод
one = input()
two = input()
count = 0
for i in range(len(one)-len(two)+1):
    if one[i:i+len(two)] == two:
        count += 1
print(count)
print(one.count(two))
