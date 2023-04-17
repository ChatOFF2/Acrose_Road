import turtle
import random
turtle.colormode(255)
class Peshehod(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.penup()
        self.setheading(90)
        self.goto(x, y)


    def move(self):
        self.forward(10)

    def olvaysmove(self):
        self.forward(10)

    def removerit(self):
        self.clear()