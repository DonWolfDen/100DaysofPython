from turtle import *
SPEED = 15


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(x, 0)
        self.setheading(90)
        self.score = 0

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


    # def move(self):
    #     while self.ycor() != 270:
    #         self.forward(5)
    #     while self.ycor() != -270:
    #         self.back(5)
