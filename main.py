from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# TODO: Create a snake body.
# TODO: Move the snake.
# TODO: Crate snake food.
# TODO: Detect collision with food.
# TODO: Create a scoreboard.
# TODO: Detect collision with wall.
# TODO: Detect collision with tail.


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.update()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_counter()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

     # if head collides with any segment in the tail:
    # trigger game_over

    snake.move()

screen.exitonclick()
