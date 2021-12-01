# created by Илья Данилов
# date 07.10.2021
# description Количество совпадающих пар

def letter_equally():
    unique = 0
    for x in range(0, max_letter):
        for y in range(x + 1, max_letter):
            if y < len(letter) and letter[x] == letter[y]:
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
        letter_equally()
