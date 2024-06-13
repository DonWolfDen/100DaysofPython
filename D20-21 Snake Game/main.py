from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

diff = screen.textinput(title="Select Difficulty", prompt="Type 1 for easy, 2 for medium, or 3 for hard").lower()
speed = {"1": 0.2, "2": 0.1, "3": 0.05}

screen.listen()
screen.onkeypress(key="w", fun=snake.go_up)
screen.onkeypress(key="a", fun=snake.go_left)
screen.onkeypress(key="s", fun=snake.go_down)
screen.onkeypress(key="d", fun=snake.go_right)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed[diff])
    snake.move()

    if snake.snake[0].distance(food) < 10:
        food.refresh()
        score.board()
        snake.extend()

    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        score.game_over()
        game_is_on = False

    for scale in snake.snake[1:]:
        if snake.snake[0].distance(scale) < 10:
            score.game_over()
            game_is_on = False


screen.exitonclick()
