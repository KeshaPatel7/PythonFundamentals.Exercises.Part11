
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_of_Rectangle(self):
        area = self.length * self.width
        return area


    def perimeter_of_Rectangle(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


rect = Rectangle(2, 4)
print(rect.area_of_Rectangle())
# 8

square = Square(8)
print(square.area_of_Rectangle())
# 64

print(square.perimeter_of_Rectangle())
# 32


