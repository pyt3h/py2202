class Rect:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_with(self):
        return self.x2 - self.x1

    def get_height(self):
        return self.y2 - self.y1

    def get_area(self):
        return self.get_with() * self.get_height()


rect = Rect()
print(rect.get_with())
print(rect.get_height())
print(rect.get_area())