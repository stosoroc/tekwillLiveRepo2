import numbers

def validate_numeric(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, numbers.Number):
            return result
        else:
            raise ValueError("The result of this function is not numeric.")
    return wrapper

@validate_numeric
def add(a, b):
    return a + b

@validate_numeric
def mul(a, b):
    return a * b

print(add(1, 2))
print(mul(2, 3))
print(add("a", "b"))
