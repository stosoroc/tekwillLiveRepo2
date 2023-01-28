from lesson_21_live.example_point import Point


class ImmutablePoint(Point):
    _locked = False

    def __init__(self, x, y):
        super().__init__(x, y)
        self._locked = True

    def __setattr__(self, key, value):
        if self._locked:
            raise Exception('Cant modify point')
        super().__setattr__(key, value)

    def __str__(self):
        return f'Point at {self.x}, {self.y}'


ip = ImmutablePoint(1, 1)
ip2 = ImmutablePoint(2, 2)

print(ip2 > ip)
print(ip)
