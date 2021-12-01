# created by Илья Данилов
# date 18.09.2021
# description Количество палиндромов

try:
    valuePol = int(float(input()))
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
else:
    if 1 <= valuePol <= 100000:
        isPol = 0
        while valuePol > 0:
            valuePolStr = valuePol.__str__()
            valuePolReverse = valuePolStr[::-1]
            # print(f'{valuePolStr} -- {valuePolReverse}')
            if valuePolStr == valuePolReverse:
                isPol += 1
            valuePol -= 1
        print(isPol)
