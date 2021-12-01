# created by Илья Данилов
# date 19.10.2021
# description Школы с наибольшим числом участников олимпиады


if __name__ == '__main__':
    total = dict()
    while True:
        try:
            listInput = list(map(str, input().split()))
            if len(listInput) == 0:
                break
            if listInput[-2] in total:
                total[listInput[-2]] += 1
            else:
                total[listInput[-2]] = 1
        except (ValueError, TypeError):
            print('Value error')
        except EOFError:
            break

    max_value = max(total.values())
    l1 = list(key for key, value in total.items() if value == max_value)
    for x in l1:
        print(x, end=' ')
