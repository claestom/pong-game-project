from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)
screen.listen()

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "a")
screen.onkey(paddle_l.go_down, "q")


game_is_one = True
while game_is_one:
    # Difficulty of the game: 1 = easy, 0.01 = hard
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Check for bounce to top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for bounce to right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Check if right paddle misses
    if ball.xcor() > 400:
        score.increase_score_l()
        ball.restart()
    # Check if left paddle misses
    if ball.xcor() < -400:
        score.increase_score_r()
        ball.restart()

screen.exitonclick()
