# created by Илья Данилов
# date 16.09.2021
# description Спички

try:
    # l1, r1, l2, r2, l3, r3 = map(float, input().split())
    l1, r1 = int(round(float(input()))), int(round(float(input())))
    l2, r2 = int(round(float(input()))), int(round(float(input())))
    l3, r3 = int(round(float(input()))), int(round(float(input())))

    # while True:
    #     if l3 < l1:
    #         l3, l1 = l1, l3
    #         r3, r1 = r1, r3
    #     elif l3 < l2:
    #         l2, l3 = l3, l2
    #         r2, r3 = r3, r2
    #     elif l2 < l1:
    #         l1, l2 = l2, l1
    #         r1, r2 = r2, r1
    #     else:
    #         break

    # print(l1, r1, l2, r2, l3, r3)

    checkValue1 = (l1 >= 0) and (l1 < r1) and (r1 <= 100)
    checkValue2 = (l2 >= 0) and (l2 < r2) and (r2 <= 100)
    checkValue3 = (l3 >= 0) and (l3 < r3) and (r3 <= 100)

    # match3_1 = ((l2 - r1) <= 1) and ((l3 - r2) > 1)
    # match3_2 = ((l2 - r1) > 1) and ((l3 - r2) > 1) and (l2 - r1) <= (r3 - l3)
    # match2_1 = l2 > l3 and l3 < l1 and (r2 - l2) >= (l1 - r3) and l3 - r1 < 1
    # match2_2 = l2 < l1 and l1 > l3 and (r2 - l2) >= (r1 - l3) and l3 - r1 < 1
    # match1_1 = (l1 > r2 and (r1 - l2) >= (l2 - r2))
    # match1_2 = ((l2 - r1) >= 1) and ((l3 - r2) <= 1)
    # match0 = ((l2 - r1) <= 1) and (((l3 - r2) <= 1) or ((l3 - r1) <= 1))

    match3_1 = ((l3 - r2) >= 1 > (l2 - r1))
    match3_2 = ((l2 - r1) >= 1) and ((l3 - r2) >= 1) and (l2 - r1) < (r3 - l3)
    match2_1 = (l2 - r1) >= 1 > (l3 - r2) and (r2 - l2) > (l3 - r1)
    match2_2 = (l3 - r2) >= 1 > (l2 - r1) and (r2 - l2) > (l3 - r1)
    match1_1 = (r2 - l3) >= 1 > (r1 - l2)
    match1_2 = ((l3 - r2) >= 1) and (r1 - l1) > (l3 - r2)
    match0 = (r2 >= l3 > r1 >= l2) or \
             (l3 <= r2 < l1 <= r3) or \
             (r2 <= r1 and r3 >= l1 < l2) or \
             (r1 >= l3 > r2 >= l1) or \
             (r2 - l2 >= l3 and r2 - l2 >= l1)

    if checkValue1 and checkValue2 and checkValue3:
        if match0:
            print(0)
        elif match3_1 or match3_2:
            if l1 > l3 > l2 or (l2 < l1 < l3 and r1 < r2 < r3):
                print(1)
            else:
                print(3)
        elif match2_1 or match2_2:
            if l1 < l2 < l3:
                print(1)
            else:
                print(2)
        elif match1_1 or match1_2:
            print(1)
        else:
            print(-1)
    else:
        print(-1)

except ValueError:
    print('Value error')
except TypeError:
    print('Type error')
