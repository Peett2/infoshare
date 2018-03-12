# index = 0
# for i in 'Kotek':
#     print('index {}'.format(index), i)
#     break
#     i += 1
# print(index)

import time
import random

def log_time(func):
    def inner():
        start = time.time()
        x = func()
        end = time.time() - start
        print(f'czas działania to {end}')
        return x
    return inner

@log_time
def foo():
    val = random.randint(1, 5)
    print('before sleep')
    time.sleep(val)
    print('after sleep')

if __name__ == '__main__':
    foo()      # inner()