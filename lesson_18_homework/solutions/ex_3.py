import time


def benchmark_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} a rulat {end_time - start_time:0.02f} secunde')
        return res

    return wrapper


@benchmark_time
def example():
    time.sleep(3)


example()
