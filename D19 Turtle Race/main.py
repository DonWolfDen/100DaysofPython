from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=400, height=400)
#bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
restart = None
# Make turtles and set to starting position

turtles = []
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color("black", colors[i])
    turtles[i].penup()

while not restart:
    y = -140
    for turtle in turtles:
        turtle.goto(x=-180, y=y)
        y += 60
    
    
    is_race_on = True
    
    while is_race_on:
        for turtle in turtles:
            rand_distance = random.randint(0, 5)
            turtle.forward(rand_distance)
            if turtle.xcor() > 160:
                is_race_on = False
                winner = turtle.fillcolor()
                restart = screen.textinput(title="Winner!", prompt=f"The {winner} turtle wins!\nHit OK to race again")



screen.exitonclick()
