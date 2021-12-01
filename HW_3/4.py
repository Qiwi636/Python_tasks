# created by Илья Данилов
# date 30.09.2021
# description Разворот последовательности

def squareNum(numString):
    try:
        num = int(input())
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        if num == 0:
            if numString == '':
                return print(0)
            else:
                return print(f'{num}\n' + numString)
        else:
            squareNum(f'{num}\n' + numString)


if __name__ == '__main__':
    someString = ''
    squareNum(someString)
