# Section 1 - Your code
from utils import *
set_background("fall")

s1 = create_sprite("sponge", 200, 200)
s2 = create_sprite("sponge", -200, 200)
s2 = create_sprite("sponge", -200, -200)
s2 = create_sprite("sponge", 200, -200)
s2 = create_sprite("sponge", 0, 0)
s2 = create_sprite("sponge", 48, -122)
s2 = create_sprite("sponge", -188, -43)
s2 = create_sprite("sponge", -59, 194)
s2 = create_sprite("sponge", 159, 47)
s2 = create_sprite("sponge", 29, 133)
s2 = create_sprite("sponge", -173, 32)
s2 = create_sprite("sponge", 150, -150)
s2 = create_sprite("sponge", -150, 150)
s2 = create_sprite("sponge", 150, 150)
s2 = create_sprite("sponge", -150, -150)
s2 = create_sprite("sponge", -32, 192)
s2 = create_sprite("sponge", 253, -250)
s2 = create_sprite("sponge", -173, 120)
s2 = create_sprite("sponge", 230, 153)
s2 = create_sprite("sponge", -120, -0)
s2 = create_sprite("sponge", -123, 32)
s2 = create_sprite("sponge", 10, -15)
s2 = create_sprite("sponge", -40, 30)
s2 = create_sprite("sponge", 20, 140)
s2 = create_sprite("sponge", -4, -120)
s2 = create_sprite("sponge", -17, 99)
s2 = create_sprite("sponge", 10, -10)
s2 = create_sprite("sponge", -10, 150)
s2 = create_sprite("sponge", 150, 10)
s2 = create_sprite("sponge", -50, -150)

message1 = create_sprite("sponge",-200,200)
message1.color("yellow")
message1.write("SPONGE",font = ("arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()