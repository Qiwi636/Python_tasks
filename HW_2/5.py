# created by Илья Данилов
# date 20.09.2021
# description Заменить пробел и группы пробелов символом "*"

try:
    # print(input().replace(' ', '*'))
    print('*'.join(input().split()))
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
