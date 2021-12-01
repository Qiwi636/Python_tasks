# created by Илья Данилов
# date 05.10.2021
# description Ферзи

def queen_move():
    no_move = 0
    for queen in gen_list:
        for any_quenn in gen_list:
            if queen != any_quenn and (queen[0] == any_quenn[0] or
                                       queen[1] == any_quenn[1] or
                                       abs(queen[0] - any_quenn[0]) ==
                                       abs(queen[1] - any_quenn[1])):
                no_move += 1

    total = print('NO') if no_move == 0 else print('YES')
    return total


if __name__ == '__main__':
    try:
        gen_list = list()
        for z in range(0, 8):
            arr = list(map(int, input().split()))
            gen_list.append(arr)
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        queen_move()
