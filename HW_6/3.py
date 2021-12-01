# created by Илья Данилов
# date 19.10.2021
# description Количество совпадающих

def count_equal(l1, l2):
    total = set.intersection(l1, l2)
    for num in total:
        print(num, end=' ')


if __name__ == '__main__':
    try:
        listInput_1 = set(map(int, input().split()))
        listInput_2 = set(map(int, input().split()))

    except (ValueError, TypeError):
        print('ERROR!')
    else:
        count_equal(listInput_1, listInput_2)
