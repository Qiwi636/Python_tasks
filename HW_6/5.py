# created by Илья Данилов
# date 23.10.2021
# description Забастовки

def strike(days, party):
    weekday = set([day for day in range(1, days + 1) if 0 < day % 7 < 6])
    total = set()
    for _ in range(party):
        try:
            quantity, gap = [int(y) for y in input().split()]
        except (ValueError, TypeError):
            print('ERROR!')
        else:
            for z in range(quantity, days + 1, gap):
                if z in weekday:
                    total.add(z)
            print(len(total))


if __name__ == '__main__':
    try:
        N, K = [int(x) for x in input().split()]
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        strike(N, K)
