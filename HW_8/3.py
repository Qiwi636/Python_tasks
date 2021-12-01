# created by Илья Данилов
# date 21.11.2021
# description Наименьший нечетный


print(min(list(filter(lambda x: x % 2 == 1, list(map(int, input().split()))))))
