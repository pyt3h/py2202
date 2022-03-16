import math
class Shape:
    def get_area(self):
        ...
    def get_perimeter(self):
        ...
    def get_ap_ratio(self):
        return self.get_area()**0.5/self.get_perimeter()

class Rect(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_area(self):
        return (self.y2-self.y1)*(self.x2-self.x1)

    def get_perimeter(self):
        return 2*(self.y2-self.y1+self.x2-self.x1)

class Circle(Shape):
    def __init__(self, x, y, r):
        ...

    def get_area(self):
        return ...

    def get_perimeter(self):
        return ...

rect = Rect(0,0,6,4)
print(rect.get_ap_ratio())

square = Rect(0,0,5,5)
print(square.get_ap_ratio())

circle = Circle(0,0,10.0)
print(circle.get_ap_ratio())
