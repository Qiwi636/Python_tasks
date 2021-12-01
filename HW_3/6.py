# created by Илья Данилов
# date 28.09.2021
# description Принадлежит ли точка квадрату

def isPointInSquare(x, y):
    return ((cor_x_start <= x <= cor_x_end) and (cor_y_start <= y <= cor_y_end) and (
            x + y != 0 and x - y != 0)) or (x == 0 and y == 0)


if __name__ == '__main__':
    try:
        cor_x_start, cor_x_end = -1, 1
        cor_y_start, cor_y_end = -1, 1
        x_sq, y_sq = int(float(input())), int(float(input()))

        if isPointInSquare(x_sq, y_sq):
            print('YES')
        else:
            print('NO')
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
