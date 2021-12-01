# created by Илья Данилов
# date 01.11.2021
# description Номер появления слова
from sys import stdin


def get_value(d, key):
    for k, v in d.items():
        if k == key:
            return v


def file_num_count():
    file_dict = dict()

    with open('file_words.txt', 'r') as fr:
        for line in fr:
            for word in line.split():
                if word in file_dict:
                    file_dict[word] += 1
                    print(get_value(file_dict, word), end=' ')
                else:
                    file_dict[word] = 0
                    print(get_value(file_dict, word), end=' ')


if __name__ == '__main__':
    try:
        with open('file_words.txt', 'w') as fw:
            stringInput = input() + '\n'
            for line1 in stdin:
                stringInput += line1
            fw.writelines(stringInput)
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        file_num_count()
