# created by Илья Данилов
# date 06.11.2021
# description Частотный анализ
from sys import stdin


def frequency_analyses():
    word_freq = dict()

    with open('file_words.txt', 'r') as fr:
        for line in fr.readlines():
            for word in line.split():
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    for elem in sorted(word_freq.items(), key=lambda x: (-x[1], x[0])):
        print(elem[0])


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
        frequency_analyses()
