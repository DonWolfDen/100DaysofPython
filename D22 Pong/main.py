from turtle import Screen
from score import UI
from paddles import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)
user = Paddle(-370)
pc = Paddle(370)
ball = Ball()
dots = UI()
dots.dots()
scoreboard = UI()

screen.listen()
screen.onkeypress(user.move_up, "w")
screen.onkeypress(user.move_down, "s")
screen.onkeypress(pc.move_up, "Up")
screen.onkeypress(pc.move_down, "Down")


gaming = True
while gaming:
    time.sleep(0.02)
    scoreboard.score(user.score, pc.score)
    screen.update()
    ball.move()
    ball.game(user, pc)


screen.exitonclick()

'''
screen
player paddle
pc paddle
moving ball
wall collision
paddle collision
missed ball
score.py
'''
