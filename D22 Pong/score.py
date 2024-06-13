from turtle import Turtle, Screen


# class Score(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.hideturtle()
#         self.pencolor("white")
#         self.goto(0, 280)
#         self.write(arg=f"{us_score}    {pc_score}", align="center", )


class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.speed(0)
        self.pensize(3)
        self.penup()
        self.hideturtle()

    def dots(self):
        self.goto(0, -290)
        self.setheading(90)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def score(self, x, y):
        self.goto(0, 230)
        self.clear()
        self.write(arg=f"{x}   {y}", align="center", font=("sans", 50, "normal"))

