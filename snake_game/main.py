from turtle import Screen
import time
from snake import Snake
from food1 import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Srinivas's  Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segment[0].distance(food) < 20:
        food.refresh()
        scoreboard.updatescore()
        snake.enlarge()

    if snake.segment[0].xcor() > 285 or snake.segment[0].xcor() < -285 or snake.segment[0].ycor() > 285 or snake.segment[0].ycor() < -285:
        scoreboard.gameover()
        scoreboard.reset()
        snake.restart()

    for x in snake.segment[1:]:
        if snake.segment[0].distance(x) < 10:
            scoreboard.gameover()
            scoreboard.reset()
            snake.restart()

screen.exitonclick()