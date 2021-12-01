# created by Илья Данилов
# date 19.10.2021
# description Количество различных чисел


def file_num_count():
    file_set = set()
    with open('file_words.txt', 'r') as fr:
        for line in fr:
            for num in line.split():
                try:
                    file_set.add(int(num))
                except ValueError:
                    pass

    return file_set


if __name__ == '__main__':
    try:
        with open('file_words.txt', 'w') as fw:
            fw.write(input())
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        print(len(file_num_count()))
