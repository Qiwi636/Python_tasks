# created by Илья Данилов
# date 13.09.2021
# description Сложное уравнение

try:
    a = int(round(float(input())))
    b = int(round(float(input())))
    c = int(round(float(input())))
    d = int(round(float(input())))

except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
else:
    if a == 0 and b == 0:
        print('INF')
    elif a == 0 or b * c == a * d:
        print('NO')
    elif b % a == 0:
        x = -b // a
        print(x)
    else:
        print('NO')
