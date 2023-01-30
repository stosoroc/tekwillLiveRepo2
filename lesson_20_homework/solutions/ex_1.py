class Shape:

    def __init__(self, border_color, inner_color):
        self._border_color = border_color
        self._inner_color = inner_color

    def get_inner_color(self):
        return self._inner_color

    def set_inner_color(self, value):
        self._inner_color = value

    def get_border_color(self):
        return self._border_color

    def set_border_color(self, value):
        self._border_color = value


class Circle(Shape):

    def __init__(self, radius, border_color, inner_color):
        super().__init__(border_color, inner_color)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value


class Rectangle(Shape):

    def __init__(self, width, length, border_color, inner_color):
        super().__init__(border_color, inner_color)
        self._width = width
        self._length = length

    def set_width(self, value):
        self._width = value

    def set_length(self, value):
        self._length = value

    def get_width(self):
        return self._width

    def get_length(self):
        return self._length


class Square(Rectangle):

    def __init__(self, side, border_color, inner_color):
        super().__init__(side, side, border_color, inner_color)

    def set_width(self, value):
        self._width = value
        self._length = value

    def set_length(self, value):
        self._length = value
        self._width = value

    def __setattr__(self, key, value, ow=False):
        super().__setattr__(key, value)
        if not ow:
            self.__setattr__('_length', value, True)
            self.__setattr__('_width', value, True)

