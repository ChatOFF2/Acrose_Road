import turtle


class Car(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.shapesize()
        self.penup()
        self.goto(x, y)

    def caremove(self):
        self.goto()

    def randomcreate10car(self):
        pass

    def move(self):
        self.forward(10)