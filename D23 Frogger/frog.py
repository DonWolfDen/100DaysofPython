from turtle import Turtle


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.up()
        self.restart()
        self.setheading(90)
        self.score = 0
        self.lives = 10

    def restart(self):
        self.goto(0, -280)

    def move_up(self):
        self.setheading(90)
        self.forward(40)

    def move_down(self):
        self.setheading(270)
        self.forward(40)

    def move_left(self):
        self.setheading(180)
        self.forward(40)

    def move_right(self):
        self.setheading(0)
        self.forward(40)
