def print_all_args(*info):
    print(*info)


def execute_with_args(func, *args):
    func(*args)


execute_with_args(print_all_args, [1, 2, 3], 123)

print(list(sorted([4, 5, 6, 7, 8, 9, 12, 2, 3], key=lambda el: el % 2)))

sum_lambda = lambda a, b: {'sum': a + b, 'diff': a - b}


# Echivalent

def sum(a, b):
    return {'sum': a + b, 'diff': a - b}


print(sum_lambda(10, 5))
print(sum(10, 5))
