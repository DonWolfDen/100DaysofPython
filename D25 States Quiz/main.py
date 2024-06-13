import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guesses = []
gaming = True
while len(guesses) < 50:
    answer = screen.textinput(title=f"{len(guesses)}/50 States Guessed",
                              prompt="Guess a state:").title()
    if answer == "Exit":
        missed = []
        for state in states:
            if state not in guesses:
                missed.append(state)

        pandas.DataFrame(missed).to_csv("states_to_learn.csv")
        break

    # for state in data.state:
    #     if state == answer and answer not in guesses:
    if answer in states and answer not in guesses:
        state = data[data.state == answer]
        pen.goto(state.x.item(), int(state.y))
        pen.write(arg=state.state.item(), align="center")
        guesses.append(answer)


pen.goto(0, 0)
pen.write(arg="You Win, nerd!", align="center", font=("courier", 50, "normal"))


turtle.mainloop()
