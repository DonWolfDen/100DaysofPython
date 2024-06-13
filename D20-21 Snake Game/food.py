from turtle import Turtle
from random import *


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed(0)
        self.refresh()

    def refresh(self):
        coordinates = []
        start = -280
        for i in range(int(600/20)-1):
            coordinates.append(start)
            start += 20
        self.goto(choice(coordinates), choice(coordinates))
