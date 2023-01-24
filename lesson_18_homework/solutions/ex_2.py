from numbers import Number


def validate_numeric(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, Number):  # Poate sa fie float, int, Decimal, complex, ...
            raise ValueError('Result is not a number')
        return result

    return wrapper


@validate_numeric
def add(a, b):
    return a + b


print(type(add))
print(add(1, 2))
