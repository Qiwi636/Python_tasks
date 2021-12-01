import random
import time
import test
from datetime import datetime

# start_time = time.time()
# print(f'\n\n{time.time() - start_time}')

def generate_rand_list():
    rand_list = list()
    for x_rand in range(0, 100000):
        rand_list.append(random.randint(-10000, 10000))

    # print(rand_list)
    return rand_list
# start_time = time.time()
#         count_sort(test.generate_rand_list())
#         print(f'\n\n{time.time() - start_time}')
