from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # default width is 4, default length is 100
        self.goto(position)

    def up(self):
        # set restriction if at top of screen
        if self.ycor() + 20 > (300-50):
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        # set restriction if at bottom of screen
        if self.ycor() -20 < (-300 + 50):
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)