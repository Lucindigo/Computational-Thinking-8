import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)
x = s1.xcor()
y = s1.ycor()
# Section 2: define controls
def move_up():
    if s1.ycor() <= 230:
        x = s1.xcor()
        y = s1.ycor() + 13
        s1.goto(x,y)
        
def move_down():
    if s1.ycor() >= -230:
        x = s1.xcor()
        y = s1.ycor() - 13
        s1.goto(x,y)
    
def move_left():
    if s1.xcor() >= -330:
        x = s1.xcor() - 13
        y = s1.ycor() 
        s1.goto(x,y)
    
def move_right():
    if s1.xcor() <= 330:
        x = s1.xcor() + 13
        y = s1.ycor() 
        s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

def draw():
    s1.pendown()
window.onkeypress(draw, "c")
def stop_drawing():
    s1.penup()
window.onkeyrelease(stop_drawing "c")
def erase():
    s1.clear
window.onkeypress(erase "q")
def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "r")
def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "g")
# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()