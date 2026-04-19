from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# when user levels up, increase by 10
MOVE_INCREMENT = 10
STARTING_X_POSITION = 300
CAR_HEADING = 180

class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.initialize_cars()

    def initialize_cars(self):
        # create starting screens with random x and y locations for some number of cars
        for _ in range(30):
            self.add_car(initialize=True)


    def add_car(self, initialize=False):
        new_car = Turtle(shape = "square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(CAR_HEADING)
        # time.sleep(random.randint(1,10))
        if initialize:
            x_coord = random.randint(-280, 280)
        else:
            x_coord = STARTING_X_POSITION
        new_car.goto(x_coord, random.randint(-250, 260))
        self.cars.append(new_car)


    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)


    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT



