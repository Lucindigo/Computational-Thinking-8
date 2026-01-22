# imports turtle time functions and random functions
import turtle, time, random
from utils import *

# Section 1 - this defines the variablles and choses the starting points of each sprite
x1 = -301
y1 = 200
x2 = -301
y2 = 100
x3 = -299
y3 = -75
x4 =-301
y4 = -200


# Section 2 - this sets the backround to cappybara sunset and creates the sprites bench cool_dog sponge and dog as well
# as setting the sprites starting position
set_background("capybara_sunset")
t1 = create_sprite("bench",x1,y1)
t2 = create_sprite("cool_dog",x2,y2)
t3 = create_sprite("sponge",x3,y3)
t4 = create_sprite("dog",x4,y4)


# Section 3 - this section moves the sprites 80 times with the sponge slightly favored because it moves
#   between 3 and 11 while the others move between 2 and 10
time.sleep(5)
for i in range(80):
    x1 += random.randint (2,10)
    x2 += random.randint (3,10)
    x3 += random.randint (3,11)
    x4 += random.randint (2,10)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)

 
# Section 4 - this section determines the winner and tells you who won with a unique message for each
if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("okay then player one wins")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins i guess")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print ("player 4 wins and im sad")
else:
    print ("yay my child won")

turtle.exitonclick()