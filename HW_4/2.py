# created by Илья Данилов
# date 07.10.2021
# description Четные индексы


def even_numbered(number, list1):
    arr = ''
    for x in range(0, number, 2):
        if len(list1) > x:
            arr += f'{list1[x]} '
    print(arr)


if __name__ == '__main__':
    try:
        num = int(input())
        listInput = list(map(int, input().split()))
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        even_numbered(num, listInput)
