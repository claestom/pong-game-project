from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
