# created by Илья Данилов
# date 18.10.2021
# description Гражданская оборона(*)

def distance(village_amount, village_list, shelter_amount, shelter_list):
    try:
        if len(village_list) != village_amount or shelter_amount != len(shelter_list):
            raise ZeroDivisionError
    except ZeroDivisionError:
        print('ERROR!')
    else:
        for v in village_list:
            min_way = 1000
            min_way_id = 0
            for s in range(0, shelter_amount):
                a, b = v, shelter_list[s]
                if b < a:
                    a, b = b, a
                if b - a <= min_way:
                    min_way = b - a
                    min_way_id = s + 1
            print(f'{min_way_id}', end=' ')


if __name__ == '__main__':
    try:
        max_village = int(input())
        village = list(map(int, input().split()))
        max_shelter = int(input())
        shelter = list(map(int, input().split()))
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        distance(max_village, village, max_shelter, shelter)
