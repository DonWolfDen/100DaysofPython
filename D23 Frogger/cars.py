import turtle
from turtle import Turtle
from random import randint, choice


class Car(Turtle):

    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("square")
        self.fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        self.pencolor((0, 0, 0))
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def restart(self, n, cars):
        posy = []    # |
        posx = [-320, 320]    # --
        for i in range(2, 14, 2):
            y = 280 - i * 40
            posy.append(y)
        for i in range(1, 15, 2):
            y = 280 - i * 40
            posy.append(y)

        if n % 2 == 0:
            self.goto(posx[0], choice(posy[:6]))
            self.setheading(0)
        else:
            self.goto(posx[1], choice(posy[6:]))
            self.setheading(180)
        self.speed = (320 + self.ycor()) / 20
        for i in range(len(cars)):
            if self.distance(cars[i]) < 40\
                    and cars[i].ycor() == self.ycor()\
                    and cars[i] != self:
                self.restart(n, cars)

    def move(self, cars):
        self.forward(int(self.speed))

        if self.xcor() > 330 or self.xcor() < -330:
            self.restart(randint(0, 1), cars)
