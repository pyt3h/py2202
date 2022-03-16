class Shape:
    def __init__(self, **kwargs):
        self.data = kwargs # {'x': 0, 'y':0, 'r':1}

rect = Shape(x1=0,y1=0, x2=5, y=6)
circle = Shape(x=0, y=0, r=2)

print(rect.data['x1']) 
print(circle.data['r'])