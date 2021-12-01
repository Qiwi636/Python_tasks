# created by Илья Данилов
# date 21.11.2021
# description Произведение пятых степеней

import functools

print((functools.reduce(lambda x, y: x * y, list(map(int, input().split())))) ** 5)
