# created by Илья Данилов
# date 10.10.2021
# description Последний максимум

def last_max(list_for_check):
    last_max_value = 0
    max_value = 0
    for x in range(0, len(list_for_check)):
        if list_for_check[x] >= max_value:
            max_value = list_for_check[x]
            last_max_value = x
    print(max_value, last_max_value)


if __name__ == '__main__':
    try:
        listCheck = list(map(int, input().split()))
    except ValueError:
        print('ERROR!')
    except TypeError:
        print('ERROR!')
    else:
        last_max(listCheck)
