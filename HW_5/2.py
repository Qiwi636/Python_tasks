# created by Илья Данилов
# date 18.10.2021
# description Сортировка подсчетом


def count_sort(a_sort):
    len_a_sort = len(a_sort)
    if len_a_sort <= 1:
        return a_sort

    centre_elem = a_sort[int(len_a_sort / 2)]

    start = list(filter(lambda elem: elem < centre_elem, a_sort))
    centre = [i for i in a_sort if i == centre_elem]
    end = list(filter(lambda elem: elem > centre_elem, a_sort))

    return count_sort(start) + centre + count_sort(end)


if __name__ == '__main__':
    try:
        listInput = list(map(int, input().split()))
    except ValueError:
        print('ERROR!')
    except TypeError:
        print('ERROR!')
    else:
        a_sorted = count_sort(listInput)
        for x in range(0, len(a_sorted)):
            print(a_sorted[x], end=' ')
