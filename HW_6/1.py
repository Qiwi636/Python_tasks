# created by Илья Данилов
# date 27.10.2021
# description Количество слов в тексте
from sys import stdin


def file_words_count():
    file_set = set()
    with open('file_words.txt', 'r') as fr:
        for line in fr.readlines():
            for word in line.split():
                file_set.add(word)
    print(file_set)
    return file_set


if __name__ == '__main__':
    try:
        with open('file_words.txt', 'w') as fw:
            stringInput = input()
            for line1 in stdin:
                stringInput += f' {line1} '
            fw.writelines(stringInput)
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        print(len(file_words_count()))
