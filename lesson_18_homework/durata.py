import time
import random

def benchmark_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f' Functia: {(func.__name__).upper()}, a durat {int(end_time - start_time)} secunde')
        return result
    return wrapper

@benchmark_time
def add(a, b):
    time.sleep(random.randint(1, 7))
    return a + b

@benchmark_time
def mul(a, b):
    time.sleep(random.randint(1, 7))
    return a * b

print("Start")
print(add(1, 2))
print(mul(2, 3))
