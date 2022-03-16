class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self, step=1):
        self.x -= step
    
    def move_right(self, step=1):
        self.x += step

    def move_up(self, step=1):
        self.y -= step

    def move_down(self, step=1):
        self.y += step

    def show_position(self):
        print(self.x, self.y)

robot = Robot(0,0)
robot.move_left()
robot.move_down(4)
robot.show_position()
robot.move_right(2)
robot.show_position()