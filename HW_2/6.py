# created by Илья Данилов
# date 18.09.2021
# description Замена фрагмента

try:
    wordStr = input().strip()
    startIndex = wordStr.find('h') + 1
    endIndex = wordStr.rfind('h') - 1
    oldWordStr = wordStr[startIndex:endIndex]
    newWordStr = wordStr[startIndex:endIndex].replace('h', 'H')
    print(wordStr.replace(oldWordStr, newWordStr))
except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
