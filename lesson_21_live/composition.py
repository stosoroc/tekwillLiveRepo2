class ColoredShape:

    def __init__(self, border_color, inner_color, gradient):
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


class Circle:

    def __init__(self, radius, color_shape: ColoredShape):
        self._radius = radius
        self.color_shape = color_shape

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value

    def __str__(self):
        return f"{self.color_shape.get_inner_color()} Circler with radius {self._radius} and {self.color_shape.get_border_color()} border."


print(Circle(10, ColoredShape('black', 'white', 'gradient')))
