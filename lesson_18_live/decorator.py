def printer_decorator(func):
    def printer():
        result = func()
        print(result)

    return printer


@printer_decorator
def example_function():
    return {'Something'}


@printer_decorator
def other_function():
    return [1, 2, 3, 4]


value = example_function()
other_function()


def empty_decorator(func):
    print(func)

    def other():
        print(func)

    return other


@empty_decorator
def sample():
    print('S1')


@empty_decorator
def sample_2():
    print('S2')


sample()
sample_2()
sample()
sample_2()


def print_exception_decorator(func):
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as ex:
            print(ex)

    return wrapped


@print_exception_decorator
def open_file(file_name):
    open(file_name)

open_file()
