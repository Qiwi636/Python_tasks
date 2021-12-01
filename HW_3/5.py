# created by Илья Данилов
# date 01.10.2021
# description Только квадраты
import math


def squareNum(numStr):
    try:
        num = int(input())
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        return 0 if num == 0 and numStr == '' else numStr.rstrip() if num == 0 else squareNum(
            f'{num} ' + numStr) if math.sqrt(num) == round(math.sqrt(num)) else squareNum(numStr)


if __name__ == '__main__':
    someString = ''
    print(squareNum(someString))
