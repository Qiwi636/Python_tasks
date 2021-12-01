# created by Илья Данилов
# date 11.11.2021
# description Выборы Государственной Думы

def result_election(dictionary, sum_people):
    total_dict = dict()
    # print(f'Изначально: {dictionary}')
    sum_party_votes = 0
    float_percent = dict()
    for e in dictionary:
        percent_party = (dictionary[e] * 450) / sum_people
        # print(percent_party - int(percent_party))
        sum_party_votes += int(percent_party)
        total_dict[e] = int(percent_party)
        float_percent[e] = (percent_party - int(percent_party))
    # print(f'Голосов: {sum_party_votes}')
    # print(f'процентная часть {float_percent}')
    for e in dictionary:
        i = e
        for p in float_percent:
            if sum_party_votes < 450:
                if float_percent[p] > float_percent[i] or (
                        float_percent[p] == float_percent[i] and dictionary[p] > dictionary[i]):
                    i = p

        if sum_party_votes < 450:
            # print(i)
            sum_party_votes += 1
            total_dict[i] += 1
            float_percent[i] = 0
        else:
            break
    # print(f'Голосов: {sum_party_votes}')
    # print(f'процентная часть {float_percent}')
    # print(f'\nитог: {total_dict}')
    for tx in total_dict:
        print(tx, total_dict[tx])


def created_votes_dict(party, peoples, dictionary):
    if party not in dictionary:
        dictionary[party] = peoples
    else:
        dictionary[party] += peoples
    # print(dictionary)


if __name__ == '__main__':
    sum_votes = 0
    party_dict = dict()
    while True:
        try:
            input_list = list(map(str, input().split()))
            party_str = ''
            for x in input_list[:-1]:
                party_str += f'{x} '
            int_people = int(input_list[-1])
            sum_votes += int_people
        except (ValueError, TypeError):
            print('ERROR!')
        except EOFError:
            result_election(party_dict, sum_votes)
            break
        else:
            created_votes_dict(party_str.strip(), int_people, party_dict)
