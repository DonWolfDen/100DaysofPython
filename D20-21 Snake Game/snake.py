import random
import turtle
from turtle import Turtle

STARTING_POSITIONS = []
X = 0
for i in range(3):
    STARTING_POSITIONS.append((-20 * i, 0))


class Snake:

    def __init__(self):
        turtle.colormode(255)
        self.snake = []
        for position in STARTING_POSITIONS:
            self.scale(position)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.snake[0].forward(20)

    def scale(self, position):
        new_scale = Turtle("square")
        new_scale.speed(0)
        new_scale.color((30, random.randint(100, 150), 30))
        new_scale.penup()
        new_scale.goto(position)
        self.snake.append(new_scale)

    def extend(self):
        self.scale(self.snake[-1].position())

    def go_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def go_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def go_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def go_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
