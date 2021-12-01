# created by Илья Данилов
# date 21.11.2021
# description Все перестановки заданной длины
import itertools

print('\n'.join(map(''.join, itertools.permutations(map(str, range(1, int(input()) + 1))))))
