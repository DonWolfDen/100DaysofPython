from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 5
        self.y = 0


    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def game(self, user, pc):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y *= -1
        if self.distance(pc) < 50 and self.xcor() > 350 and self.x > 0:
            self.y = round(self.distance(pc) / 10)
            if self.ycor() < pc.ycor():
                self.y *= -1
            self.x *= -1
        if self.distance(user) < 50 and self.xcor() < -350 and self.x < 0:
            self.y = round(self.distance(user) / 10)
            if self.ycor() < user.ycor():
                self.y *= -1
            self.x *= -1
        if self.xcor() > 400:
            user.score += 1
            self.goto(0, 0)
            self.x *= -1
            self.y *= -1
        if self.xcor() < -400:
            pc.score += 1
            self.goto(0, 0)
            self.x *= -1
            self.y *= -1
