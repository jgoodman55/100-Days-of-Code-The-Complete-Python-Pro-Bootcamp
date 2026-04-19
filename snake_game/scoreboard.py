from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def get_high_score(self):
        with open("data.txt") as data:
            return int(data.read())

    def store_high_score(self):
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
        self.score = -1
        self.refresh_score()
