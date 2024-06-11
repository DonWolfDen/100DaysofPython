import turtle as t
import random

### Extract colors from picture
## Add any image to source folder and set it as 'image.jpg'
# import colorgram
# t.colormode(255)
# colors = colorgram.extract('image.jpg', 8)
# colors_tups = []
# for i in colors:
#     colors_tups.append(i.rgb)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

### set variables
dot = 3
w = 784
gap = dot * 2
w_dots = round((w / gap) + 1)
h_dots = round((w_dots * 0.80) + 1)

### Make timmy and set attributes
timmy = t.Turtle()
timmy.hideturtle()
timmy.speed(0)
timmy.up()
timmy.pensize(dot)

### get to starting point
timmy.back(408 - dot*2)
timmy.setheading(270)
timmy.forward(315 - dot*2)
timmy.setheading(0)

### make dots
for _ in range(h_dots):
    ## horizontal line of dots
    for _ in range(w_dots):
        timmy.pencolor(random.choice(colors))    #(colors_tups)
        timmy.dot()
        timmy.forward(gap)
    ## move up a line and return to left side
    timmy.back(w_dots * gap)
    timmy.setheading(90)
    timmy.forward(gap)
    timmy.setheading(0)


# Display
screen = t.Screen()
screen.exitonclick()
