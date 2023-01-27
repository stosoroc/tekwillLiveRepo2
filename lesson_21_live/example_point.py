class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at {self.x}, {self.y}'

    def __bool__(self):
        return self.x != 0 and self.y != 0

    @classmethod
    def _validate_instance(cls, other):
        print('Validating fro class ', cls)
        if not isinstance(other, cls):
            raise TypeError(f'Other must be point instance not {other.__class__.__name__}')

    def __getitem__(self, item):
        if item == 'x' or item == 0:
            return self.x
        if item == 'y' or item == 1:
            return self.y
        raise ValueError(f'{item} does not belong to point')

    def __setitem__(self, key, item):
        if key == 'x' or key == 0:
            self.x = item
            return
        if key == 'y' or key == 1:
            self.y = item
            return
        raise ValueError(f'{key} does not belong to point')

    # Arithmetic methods

    def __add__(self, other):
        self._validate_instance(other)
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        self._validate_instance(other)
        return Point(self.x - other.x, self.y - other.y)

    # Comparison Methods
    def __lt__(self, other):  # Less than
        self._validate_instance(other)
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
        return False

    def __gt__(self, other):  # Greater than
        self._validate_instance(other)
        if self.x > other.x:
            return True
        elif self.x == other.x:
            if self.y > other.y:
                return True
        return False

    def __eq__(self, other):  # equals comparison
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # Not equal
        return not self == other

    def __le__(self, other):  # Lower or equals
        return self == other or self < other

    def __ge__(self, other):  # Greater or equals
        return self == other or self > other


class ColoredPoint(Point):
    pass


print(isinstance(ColoredPoint(1, 1), Point))

p1 = Point(1, 1)
p2 = Point(1, 1)
p3 = Point(3, -2)
print(p1)

print(p1 == p2)
print(p1 < p2)
print(p2 >= p1)
print(p3 == p2)
print(p3 < p2)

p_0 = Point(0, 0)

if p_0:  # Equivalent cu p_0 is not None
    print('Yeey')

if p3:
    print('Yeey P3')

print(p_0 - p3)
print(p_0 + p3)

print(p3[0])
print(p3['y'])

p3['y'] -= 1

print(p3['y'])
print(p3)
