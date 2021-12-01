# created by Илья Данилов
# date 04.10.2021
# description Почти отсортирован

def isPossible(listForCheck):
    max_del = True
    for elem in range(0, len(listForCheck)):
        if elem < len(listForCheck) - 1:
            if listForCheck[elem] <= listForCheck[elem + 1]:
                if len(listForCheck) == elem + 2:
                    print('YES')
            else:
                if max_del:
                    if len(listForCheck) == elem + 2:
                        print('YES')
                    max_del = False
                else:
                    print('NO')
                    break


if __name__ == '__main__':
    try:
        listCheck = list(map(int, input().split()))
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        isPossible(listCheck)
