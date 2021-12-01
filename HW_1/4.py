# created by Илья Данилов
# date 13.09.2021
# description Ход короля

try:
    x1 = int(round(float(input())))
    y1 = int(round(float(input())))
    x2 = int(round(float(input())))
    y2 = int(round(float(input())))

    # x_possibility = x1 == (x2 - 1) or x1 == (x2 + 1) or x1 == x2
    # y_possibility = y1 == (y2 - 1) or y1 == (y2 + 1) or y1 == y2
    # if x_possibility and y_possibility:
    if -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1:
        print('YES')
    else:
        print('NO')
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
