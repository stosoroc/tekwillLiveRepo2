from lesson_21_homework.solutions.ex_1.Circle import Circle
from lesson_21_homework.solutions.ex_1.Rectangle import Rectangle
from lesson_21_homework.solutions.ex_1.Square import Square


class ShapeService:
    DEFAULT_INNER_COLOR = 'white'
    DEFAULT_OUTER_COLOR = 'black'

    @staticmethod
    def create_default_circle(radius):
        return Circle(radius, inner_color=ShapeService.DEFAULT_INNER_COLOR,
                      border_color=ShapeService.DEFAULT_OUTER_COLOR)

    @staticmethod
    def create_default_square(side_length):
        return Square(side_length, inner_color=ShapeService.DEFAULT_INNER_COLOR,
                      border_color=ShapeService.DEFAULT_OUTER_COLOR)

    @staticmethod
    def create_default_rectangle(width, length):
        return Rectangle(width, length, inner_color=ShapeService.DEFAULT_INNER_COLOR,
                         border_color=ShapeService.DEFAULT_OUTER_COLOR)

    @staticmethod
    def color_shapes(shapes, color_inner, color_outer):
        for shape in shapes:
            shape.set_inner_color(color_inner)
            shape.set_border_color(color_outer)


circ = ShapeService.create_default_circle(1)
rect = ShapeService.create_default_rectangle(10, 5)
print(circ, rect)
