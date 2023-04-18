import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("hiscore.txt", mode="r") as file:
            hiscorefromfile=file.read()
            self.hiscore=hiscorefromfile
        self.score=0
        self.hideturtle()
        self.goto(0, 350)
        self.write(f"Ваш счет = {self.score}!  Максимальный счет = {self.hiscore}", align="center")

    def prirostscheta(self):
        self.clear()
        self.score+=1
        self.write(f"Ваш счет = {self.score} Максимальный счет = {self.hiscore}", align="center")

    def savehiscore(self):
        with open("hiscore.txt", "w") as file:
            file.write(str(self.score))