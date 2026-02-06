#this is a clicker game where you can click space to increece your dogs coolness and use that coolness to buy and upgrade farms which give you coolness every second
import turtle, time, random
from utils import *
coolness = 0
coolness_click = 100
coolness_second = 0
farms = 0
farm_cost = 4000
farm_level = 0
farm_upgrade_cost = 20000
farm_coolness_second = 0.25
x1 = 0
y1 = 0
dog = create_sprite("dog", x1, y1)
# Section 1 - setup
# TODO - set a background using set_background()
set_background("grass_field")


# TODO - create at least two variables and set their starting value. ex: cookies = 0


#Section 2 - controls
#TODO - define an action. ex: def my_control()
def luca_click():
    global coolness, coolness_click
    coolness += coolness_click
    # print("(test)")
window.onkeypress(luca_click, "space")

def buy_farm():
    global farms, coolness, farm_cost, coolness_second, farm_coolness_second
    if coolness >= farm_cost:
        farms += 1
        coolness -= farm_cost
        coolness_second += farm_coolness_second
        farm_cost *= 1.25
window.onkeypress(buy_farm, "b")

def upgrade_farms():
    global farm_level, coolness, farm_level_upgrade_cost, farm_coolness_second
    if coolness >= farm_upgrade_cost:
        farm_level += 1
        coolness -= farm_upgrade_cost
        farm_level_upgrade_cost *= 3
        farm_coolness_second *= 1.5
window.onkeypress(upgrade_farms, "u")
sprite1 = create_sprite("alien", -350, 250)
sprite1.color("black")
sprite1.hideturtle()
sprite2 = create_sprite("alien", -350, 225)
sprite2.color("black")
sprite2.hideturtle()
sprite3 = create_sprite ("alien", -350, 200)
sprite3.color("black")
sprite3.hideturtle()
window.listen()
for i in range(10000000000):
    if coolness < 10000:
        set_image(dog,"dog")
        coolness_click = 50
    elif 10000 <= coolness < 1000000:
        set_image(dog, "cool_dog")
        coolness_click = 500
    elif 1000000 <= coolness < 10000000:
        set_image(dog, "really_cool_dog")
        coolness_click = 2500
    elif 10000000 <= coolness < 100000000:
        set_image(dog, "king_dog")
        coolness_click = 12500
    sprite1.clear()
    sprite1.write(f"coolness = {coolness}, coolness per click = {coolness_click}", font = ("comic sans",20, "normal"))
    sprite2.clear()
    sprite2.write(f"coolness farms = {farms}, farm level = {farm_level}", font = ("comic sans", 20, "normal"))
    sprite3.clear()
    sprite3.write(f"farm cost = {farm_cost}, farm upgrade cost = {farm_upgrade_cost}", font = ("comic sans",20, "normal"))
    coolness += coolness_second
    time.sleep(0.01)
    window.update()