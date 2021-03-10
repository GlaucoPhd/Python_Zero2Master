# Decorater
from time import time


def performace(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t1-t2} s')
        return result
    return wrapper
print('1 - Example 1 - (Store Value in Range are Faster dont take space in memory otherwise List takes.)','\n')
@performace
def long_time():
    print('1 Faster')
    for i in range(1000000):
        i * 5

@performace
def long_time2():
    print('2 Slower - * Also can kill the process')
    for i in list(range(1000000)):
        i * 5


long_time()
long_time2()
