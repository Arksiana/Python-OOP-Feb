import functools
from time import time


def uppercase(func):
    @functools.wraps(func)
    def wrapper(name):
        return func(name).upper()

    return wrapper


def measure_time(func):
    @functools.wraps(func)
    def wrapper():

        start = time()
        result = func()
        end = time()
        print(f'{func.__name__} executed in {end} {start} seconds')
        return result

    return wrapper


@uppercase
@measure_time
def get_hello_message(name):
    return f"Hello, I'm {name}"


@uppercase
def get_current_temperature():
    return '3\' celsius'


@measure_time
def big_loop():
    x = 0
    for _ in range(100000):
        x += 1



print(get_hello_message('Pesho'))
print(get_current_temperature())
print(get_current_temperature)
big_loop()