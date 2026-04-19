from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
# screen.update()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.increase_speed()

    # Detect ball passing right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect ball passing left paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()



screen.exitonclick()