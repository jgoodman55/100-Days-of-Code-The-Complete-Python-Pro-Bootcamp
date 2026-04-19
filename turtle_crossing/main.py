import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # Detect crossing finish line
    if player.cross_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.refresh_level()

    # Detect car moving off screen
        # if off screen, make another car
    for car in car_manager.cars:
        # Detect collision with car
        if (abs(car.xcor()) < 25) and (abs(car.ycor() - player.ycor()) < 15):
            game_is_on = False
            scoreboard.game_over()
            # player.reset_position()

        if car.xcor() < -320:
            car.hideturtle()
            # add a new car
            car_manager.add_car()
            # remove current car
            car_manager.cars.remove(car)


screen.exitonclick()

