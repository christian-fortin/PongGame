# Simple Ping in Python 3

import turtle

window = turtle.Screen()
window.title("Pong by Christian")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# this^ stops the window from automatically updating and so we manually update it and speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
#turtle is the module
# Turtle() is the classname
paddle_a.speed(0)
# Speed of animation
paddle_a.shape("square")
# by default the shape is 20px by 20px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
# -350 is to the left side.

# Paddle B
paddle_b = turtle.Turtle()
#turtle is the module
# Turtle() is the classname
paddle_b.speed(0)
# Speed of animation
paddle_b.shape("square")
# by default the shape is 20px by 20px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
# 350 is to the right side.

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
# ball movement speed:
ball.dx = 2.3
ball.dy = -2.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

# Functions:
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    # adds 20px to y cordinate 
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    # adds 20px to y cordinate 
    paddle_a.sety(y)
    
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    # adds 20px to y cordinate 
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    # adds 20px to y cordinate 
    paddle_b.sety(y)
    

# Keyboard binding
window.listen()
# listens for keyboard input
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")





# Main Portion of the Game
 # Every time the loop runs it updates the screen
while True:
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
   

    # Border checking:
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390: 
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390: 
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1  
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball Collisions:
    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40): 
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340  and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40): 
        ball.setx(-340)
        ball.dx *= -1
    
    
    
    