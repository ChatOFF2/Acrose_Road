import turtle

class Score(turtle.Turtle):
    schetchik=0
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.write(f"Ваш счет = {self.schetchik}")

    def prirostscheta(self):
        self.clear()
        self.schetchik+=1
        self.write(f"Ваш счет = {self.schetchik}")