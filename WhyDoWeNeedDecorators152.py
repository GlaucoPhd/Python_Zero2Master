# Library time test how much time will take to perform the task
# relayed on the machine performance


from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, *kwargs)
        t2 = time()
        print(f'took {t2-t1} miliseconds')
        return result
    return wrapper



@performance
def long_time():
    for i in range(100000000):
        i * 5

long_time()