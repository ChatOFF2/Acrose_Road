import turtle

class Peshehod(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x, y)


    def move(self):
        self.forward(10)

    def olvaysmove(self):
        self.forward(10)