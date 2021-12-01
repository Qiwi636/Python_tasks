# created by Илья Данилов
# date 30.09.2021
# description Алгоритм Евклида

def gcd(a, b):
    total = print(a + b) if a == 0 or b == 0 else gcd(a % b, b) if a > b else gcd(a, b % a)
    return total


if __name__ == '__main__':
    try:
        first, second = int(input()), int(input())
    except ValueError:
        print('Value error')
    except TypeError:
        print('Type error')
    else:
        gcd(first, second)
