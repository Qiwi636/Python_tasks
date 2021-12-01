# created by Илья Данилов
# date 20.09.2021
# description Идеальный исполнитель

try:
    a, b = int(float(input())), int(float(input()))

    while a != b:
        c = a if (a == b) else print('-1') if (a % 2 != 0 or a / 2 < b) else print(':2')
        a = a if (a == b) else a - 1 if (a % 2 != 0 or a / 2 < b) else int(a / 2)
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
