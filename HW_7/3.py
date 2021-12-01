# created by Илья Данилов
# date 02.11.2021
# description Контрольная по ударениям

def get_value(d, key):
    for k, v in d.items():
        if k == key:
            return v


def word_accent(words, lower_words):
    try:
        line_input = input()
        line_str = list()
        error_value = 0
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        for y in line_input.split():
            line_str.append(y.lower())
            if y.lower() in lower_words:
                if y in words.values():
                    pass
                else:
                    error_value += 1
            else:
                if sum(map(str.isupper, y)) == 1:
                    pass
                else:
                    error_value += 1
        print(error_value)


if __name__ == '__main__':
    try:
        word_dict = dict()
        word_list = list()
        word_count = int(input())
        for x in range(0, word_count):
            word_dict[x] = input()
            word_list.append(word_dict[x].lower())

    except (ValueError, TypeError):
        print('ERROR!')
    else:
        word_accent(word_dict, word_list)
