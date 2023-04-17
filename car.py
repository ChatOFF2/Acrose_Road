import turtle


class Car(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(0.3, 0.2)
        self.penup()
        self.goto(x, y)

    def caremove(self):
        self.goto()

    def randomcreate10car(self):
        pass
