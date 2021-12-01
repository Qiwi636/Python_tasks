# created by Илья Данилов
# date 30.09.2021
# description Рекурсивное сложение

def sum_x(num_x, res):
    final = res if num_x <= 0 else sum_x(num_x - 1, res + 1)
    return final


if __name__ == '__main__':
    try:
        a, b = int(input()), int(input())
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        print(sum_x(b, a))
