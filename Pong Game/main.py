from turtle import Screen,Turtle
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong Game❤️😃")
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.tracer(0)

turtle = Turtle("square")
turtle.goto(x=0,y=294)
turtle.color("white")
turtle.pensize(5)
turtle.hideturtle()
turtle.setheading(270.0)
for i in range(10):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.forward(20)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")
screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision of the ball  with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()
    if ball.xcor()>380 or ball.xcor() < -380:
        ball.bounce_side()

    #Detect collision with r_paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_side()

    #Detect when right paddle missed the ball.
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detedt when left paddle missed the ball.
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()