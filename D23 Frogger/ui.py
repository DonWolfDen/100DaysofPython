from turtle import Turtle


class UI(Turtle):
    def __init__(self):
        super(UI, self).__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.up()

    def endzones(self):
        self.goto(-300, -280)
        for _ in range(int(600/20)):
            self.stamp()
            self.forward(20)
        self.goto(-300, 280)
        for _ in range(int(600/20)):
            self.stamp()
            self.forward(20)

    def lanes(self):
        self.goto(-310, -300)
        for _ in range(int(600/40)):
            self.down()
            self.goto(290, self.ycor())
            self.up()
            self.goto(-310, self.ycor()+40)

    def write_score(self, frog):
        self.goto(-280, 260)
        self.pencolor("white")
        self.clear()
        self.write(arg=f"Score: {frog.score}", align="left", font=("courier", 20, "normal"))

    def write_lives(self, frog):
        self.goto(280, 260)
        self.pencolor("white")
        self.clear()
        self.write(arg=f"{frog.lives} :Lives", align="right", font=("courier", 20, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.pencolor("black")
        self.write(arg="GAME OVER", align="center", font=("courier", 50, "bold"))

    def winner(self):
        self.goto(0, 0)
        self.pencolor("black")
        self.write(arg="YOU WIN", align="center", font=("courier", 50, "bold"))
