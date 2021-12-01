# created by Илья Данилов
# date 18.09.2021
# description Вставка символа

try:
    wordStr, newWordStr = input().strip(), ''
    for x in wordStr:
        newWordStr += x + '*'
    print(newWordStr[:-1])
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
