from turtle import Turtle

WIDTH = 20
STRETCH_LEN = 5


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(coordinates)
        self.color("white")
        self.shapesize(5, 1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self. xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
