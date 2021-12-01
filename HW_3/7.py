# created by Илья Данилов
# date 30.09.2021
# description Принадлежит ли точка области?

def isPointInArea(x, y):
    return (y - 2 * x >= 2 and x + y >= 0 and abs(x + 1) ** 2 + abs(y - 1) ** 2 <= 4) or \
           (y - 2 * x <= 2 and x + y <= 0 and abs(x + 1) ** 2 + abs(y - 1) ** 2 >= 4)


if __name__ == '__main__':
    try:
        x_sq, y_sq = float(input()), float(input())
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        if isPointInArea(x_sq, y_sq):
            print('YES')
        else:
            print('NO')
