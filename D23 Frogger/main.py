from turtle import Screen
from cars import Car
from frog import Frog
from ui import UI
import time
from random import *


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)

frog = Frog()
cars = []
for i in range(20):
    cars.append(Car())
    cars[i].restart(i, [])

layout = UI()
layout.endzones()
layout.lanes()
score = UI()
lives = UI()

screen.listen()
screen.onkeypress(fun=frog.move_up, key="w")
screen.onkeypress(fun=frog.move_down, key="s")
screen.onkeypress(fun=frog.move_left, key="a")
screen.onkeypress(fun=frog.move_right, key="d")


gaming = True
while gaming:
    time.sleep(0.1)
    for i in range(len(cars)):
        cars[i].move(cars)
        if cars[i].distance(frog) < 20 and cars[i].ycor() == frog.ycor():
            frog.restart()
            frog.lives -= 1
        if frog.ycor() > 300:
            frog.restart()
            frog.score += 1
    lives.write_lives(frog)
    score.write_score(frog)

    if frog.lives == 0:
        gaming = False
        layout.gameover()
        screen.update()
    if frog.score == 10:
        gaming = False
        layout.winner()
    screen.update()

screen.exitonclick()

'''
Screen setup
make cars
make cars move
make frog.py
make frog.py move
detect collision with car and restart
add lives tracker
detect collision with top wall
score and restart

'''
