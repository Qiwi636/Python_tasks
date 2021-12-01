# created by Илья Данилов
# date 14.09.2021
# description ШАШКИ

try:
    start_x = int(round(float(input())))
    start_y = int(round(float(input())))
    end_x = int(round(float(input())))
    end_y = int(round(float(input())))
    
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
else:
    if 8 >= start_x > 0 and 8 >= start_y > 0 and 8 >= end_x > 0 and 8 >= end_y > 0 and start_y != end_y:
        while start_y != 9:
            if end_x > start_x and end_y > start_y:
                start_x += 1
                start_y += 1
            elif end_x < start_x and end_y > start_y:
                start_x -= 1
                start_y += 1
            elif end_x == start_x and end_y > start_y:
                start_y += 1
            elif end_x == start_x and end_y == start_y:
                print('YES')
                break
            else:
                print('NO')
                break
    else:
        print('NO')
