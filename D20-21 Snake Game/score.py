from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGN, font=FONT )


    def board(self):
        self.clear()
        self.score += 1
        self.update()


