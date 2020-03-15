class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
         return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, side):
        self.length = side
        self.width = side



rect1 = Rectangle(3,7)
print(rect1.area())
print(rect1.perimeter())

sq1 = Square(5)
print(sq1.area())
print(sq1.perimeter())






