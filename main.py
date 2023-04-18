import turtle
import time
import scoreboard
import car
import random
import peshehod

turtle.tracer(0)
nycar=car.Car(-300, 150)



turtle.listen()
turtle.onkey(nycar.move, "space")
scoree=scoreboard.Score()

#player=peshehod.Peshehod(0, -250)
#player2=peshehod.Peshehod(-200, -259)
#turtle.onkey(player.move, "space")

kolich=[]
GameON=True
while GameON:
    turtle.update()
    time.sleep(0.1)
    if len(kolich)<10:
        randomx=random.randint(-250, 250)
        player=peshehod.Peshehod(randomx, random.randint(-300, -50))
        kolich.append(player)
    for all in kolich:
        if nycar.distance(all)<20:
            print("GAME OVER")
            nycar.reset()

    for all in kolich:
        if all.ycor()>250:
            all.removerit()
            kolich.remove(all)
        all.olvaysmove()

    if nycar.xcor()>300:
        scoree.prirostscheta()
        scoree.savehiscore()
        nycar.car_reset()
















turtle.exitonclick()