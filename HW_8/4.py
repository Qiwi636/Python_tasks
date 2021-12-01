# created by Илья Данилов
# date 21.11.2021
# description Реализация XOR

print(*map(lambda x: int(x[0] != x[1]), zip(input().split(), input().split())))

