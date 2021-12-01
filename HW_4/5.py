# created by Илья Данилов
# date 07.10.2021
# description Больше соседей

def letter_better(number, list1):
    unique = 0
    for x in range(1, number):
        if len(list1) - 1 > x and list1[x] > list1[x + 1] and list1[x] > list1[x - 1]:
            unique += 1
    print(unique)


if __name__ == '__main__':
    try:
        max_letter = int(input())
        letter = [int(num) for num in input().split()]
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        letter_better(max_letter, letter)
