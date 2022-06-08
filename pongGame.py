# Simple Ping in Python 3

import turtle

window = turtle.Screen()
window.title("Pong by Christian")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)
# this^ stops the window from automatically updating and so we manually update it and speeds up the game

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


# Functions:
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    # adds 20px to y cordinate 
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    # adds 20px to y cordinate 
    paddle_a.sety(y)
    
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    # adds 20px to y cordinate 
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
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
while True:
    window.update()
    # Everytime the loop runs it updates the screen
