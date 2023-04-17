import turtle
import time
from car import Car
import random
turtle.tracer(0)

import peshehod

turtle.listen()

#player=peshehod.Peshehod(0, -250)
#player2=peshehod.Peshehod(-200, -259)
#turtle.onkey(player.move, "space")

kolich=[]
GameON=True
while GameON:
    turtle.update()
    time.sleep(0.1)
    if len(kolich)<30:
        randomx=random.randint(-250, 250)
        player=peshehod.Peshehod(randomx, random.randint(-300, -250))
        kolich.append(player)
    for all in kolich:
        if all.ycor()>250:
            kolich.remove(all)


        all.olvaysmove()














turtle.exitonclick()