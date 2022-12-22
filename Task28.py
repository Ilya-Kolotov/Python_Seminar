# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#
# 1) с помощью математических формул нахождения корней квадратного уравнения
#
# 2) с помощью дополнительных библиотек Python

a = 1
b = -3
c = -4
D = b ** 2 - 4 * a * c

root = []
if D < 0:
    print('No root')
elif D > 0:
    x1 = (-b - D ** 0.5) / 2 * a
    root.append(x1)
    x2 = (-b + D ** 0.5) / 2 * a
    root.append(x2)
elif D == 0:
    x1 = -b/ 2 * a
    root.append(x1)

print(root)