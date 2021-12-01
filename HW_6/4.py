# created by Илья Данилов
# date 19.10.2021
# description Пересадки

def transfer(buses):
    if buses[0] > buses[1]:
        buses[0], buses[1] = buses[1], buses[0]
    if buses[2] > buses[3]:
        buses[2], buses[3] = buses[3], buses[2]

    station = 0
    for bus1 in range(buses[0], buses[1] + 1):
        for bus2 in range(buses[2], buses[3] + 1):
            if bus1 == bus2:
                station += 1
    return station


if __name__ == '__main__':
    try:
        listInput = list(map(int, input().split()))
        # true_listInput = set(listInput)
        # if len(true_listInput) != 4:
        #     raise ValueError

    except (ValueError, TypeError):
        print('ERROR!')
    else:
        print(transfer(listInput))
