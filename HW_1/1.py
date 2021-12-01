# created by Илья Данилов
# date 13.09.2021
# description Складирование ноутбуков

x = 0
perimetr = 1
while x < 3:
    perimetr *= int(input())
    x += 1

boxsize = 1
while x > 0:
    boxsize *= int(input())
    x -= 1

print(int(perimetr/boxsize))
