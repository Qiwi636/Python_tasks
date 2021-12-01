# created by Илья Данилов
# date 18.09.2021
# description Перестановка слов

try:
    wordStr = input().strip()
    index = wordStr.find(' ')
    wordStrLen = len(wordStr) - 1
    last = wordStr[index + 1:wordStrLen+1]
    first = wordStr[0:index]
    print(f'{last} {first}')

except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
