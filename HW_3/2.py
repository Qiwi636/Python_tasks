# created by Илья Данилов
# date 30.09.2021
# description Сумма факториалов

def fact(fact_num):
    res = 1
    sum1 = 0
    for x in range(1, fact_num + 1):
        res *= x
        sum1 += res
    return sum1


if __name__ == '__main__':
    try:
        num = int(input())
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        print(fact(num))
