class Shape:
    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color
    
    def get_inner_color(self):
        return self._inner_color
    
    def set_inner_color(self, inner_color):
        self._inner_color = inner_color
    
    def get_border_color(self):
        return self._border_color
    
    def set_border_color(self, border_color):
        self._border_color = border_color

class Circle(Shape):
    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius

class Rectangle(Shape):
    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length
    
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        self._width = width
    
    def get_length(self):
        return self._length
    
    def set_length(self, length):
        self._length = length

class Square(Rectangle):
    def __init__(self, inner_color, border_color, width):
        super().__init__(inner_color, border_color, width, width)
    
    def set_length(self, length):
        self._length = length
        self._width = length
    
    def set_width(self, width):
        self._length = width
        self._width = width
        

forme = Shape("red","green")
print(forme.get_inner_color())
print(forme.get_border_color())


cerc = Circle("coral","light green",10)
print(cerc.get_inner_color())
print(cerc.get_border_color())
print(cerc.get_radius())

dreptunghi = Rectangle("indigo","blue",7,9)
print(dreptunghi.get_inner_color())
print(dreptunghi.get_border_color())
print(dreptunghi.get_width())
print(dreptunghi.get_length())

patrat = Square("black","yellow",10)

print(patrat.get_inner_color())
print(patrat.get_border_color())
print(patrat.get_width())

patrat.set_length(11)
print(patrat.get_length())