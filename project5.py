import turtle, math, time, random
from utils import *
x1 = 0
y1 = -200
x2 = 0
y2 = 200
p1_it = 1
p2_it = 0
p1_tagged_time = 0
p2_tagged_time = 0
# Section 1: Setup
p1 = create_sprite ("cool_dog", x1, y1)
p2 = create_sprite ("dog", x2, y2)
sprite_list = ["cool_dog", "dog"]
set_background ("grass_field")

def p1_move_right():
    if p1.xcor() < 350:
        x1 = p1.xcor()+5
        y1 = p1.ycor()
        p1.goto(x1,y1)
window.onkeypress(p1_move_right, "d")

def p1_move_down():
    if p1.ycor() < 275:
        y1 = p1.ycor()-5
        x1 = p1.xcor()
        p1.goto(x1,y1)
window.onkeypress(p1_move_down, "s")

def p1_move_left():
    x1 = p1.xcor()-5
    y1 = p1.ycor()
    p1.goto(x1,y1)
window.onkeypress(p1_move_left, "a")

def p1_move_up():
    y1 = p1.ycor()+5
    x1 = p1.xcor()
    p1.goto(x1,y1)
window.onkeypress(p1_move_up, "w")


def p2_move_right():
    x2 = p2.xcor()+5
    y2 = p2.ycor()
    p2.goto(x2,y2)
window.onkeypress(p2_move_right, "l")

def p2_move_down():
    y2 = p2.ycor()-5
    x2 = p2.xcor()
    p2.goto(x2,y2)
window.onkeypress(p2_move_down, "k")

def p2_move_left():
    x2 = p2.xcor()-5
    y2 = p2.ycor()
    p2.goto(x2,y2)
window.onkeypress(p2_move_left, "j")

def p2_move_up():
    y2 = p2.ycor()+5
    x2 = p2.xcor()
    p2.goto(x2,y2)
window.onkeypress(p2_move_up, "i")

s1 = create_sprite ("alien", -350, 250)
s1.color("black")
s1.hideturtle
s2 = create_sprite ("alien", -350, 200)
s2.color("black")
s2.hideturtle

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    s1.clear()
    s1.write (f"player 1 has {p1_tagged_time} tagged time", font = ("comic_sans", 20, "normal"))
    s2.clear()
    s2.write (f"player 2 has {p2_tagged_time} tagged time", font = ("comic_sans", 20, "normal"))

    if p1_it == 1:
        p1_tagged_time += 1
        if get_distance (p1,p2) < 50:
            p2_it += 1
            p1_it -= 1

    if p2_it == 1:
        p2_tagged_time += 1
        if get_distance (p1,p2) < 50:
            p1_it -= 1
            p2_it +=1
 
    # TODO - add code for automatic actions


    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")