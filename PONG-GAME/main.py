from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from pong import Pong
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

score_board = ScoreBoard()
ball = Ball()
l_pong = Pong((-350,0))
r_pong = Pong((350,0))






screen.listen()
screen.onkey(key="Up",fun=r_pong.go_up)
screen.onkey(key="Down",fun=r_pong.go_down)
screen.onkey(key="w",fun=l_pong.go_up)
screen.onkey(key="s",fun=l_pong.go_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pong) < 50 and ball.xcor() > 320:
         ball.bounce_x()
    if ball.distance(l_pong) < 50 and ball.xcor() < -320:
         ball.bounce_x()
    
    if ball.xcor() > 380:
         ball.reset_position()
         score_board.update_l_score()
    if ball.xcor() < -380:
         ball.reset_position()
         score_board.update_r_score()
         
         
   


screen.exitonclick()




