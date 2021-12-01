# created by Илья Данилов
# date 20.10.2021
# description Максимальный балл по классам

def comparison(num_cl, students):
    id_max = list()
    max_score = 0
    for student in students:
        if int(student[-2]) == num_cl:
            if int(student[-1]) >= max_score:
                max_score = int(student[-1])
                id_max = student
    return id_max[-1]


if __name__ == '__main__':
    list_of_lists = list()
    while True:
        try:
            listInput = list(map(str, input().split()))
            if len(listInput) == 0:
                break
            list_of_lists.append(listInput)
        except (ValueError, TypeError):
            print('Value error')
        except EOFError:
            break
    for x in range(9, 12):
        print(comparison(x, list_of_lists), end=' ')
