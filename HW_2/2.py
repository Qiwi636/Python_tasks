# created by Илья Данилов
# date 29.09.2021
# description Простая проверка слов

try:
    i = 10
    value = 0

    while i > 0:
        wordStr = input().strip()
        findS = (wordStr[:1] == 'S')
        if len(wordStr) == 6 and findS:
            for x in wordStr:
                if x == 'i':
                    value += 1
                    break
        i -= 1
    print(value)
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
