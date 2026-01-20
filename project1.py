correct_points = 0
incorrect_points = 0
name = input("What is your name: ")
print(f"Hello {name}, lets play 2 truths and a lie. you need to guess the lie, just press enter to continue")
input()
print("Fact #1 I have never gone to another state.") #lie
input()
print("Fact #2 I have one dog and nothing else.") #true
input()
print("Fact #3 I have met my great grandparents.") #true
input()
print("Now its time to guess type 1 for #1, 2 for #2, and 3 for #3.") #1 is correct

answer = input ("")
if answer == "1":
    correct_points += 1
    print("Correct i have been to several other states")
if answer == "2":
    incorrect_points += 1
    print("Incorrect, the answer was #1 i only have one dog but i used to have more animals")
if answer == "3":
    incorrect_points += 1
    print("Incorrect, the answer was #1 i did meet my great grandparents")

input()
print(f"{correct_points} correct")
print(f"{incorrect_points} incorrect")

input()
print("Okay time for a new round")
input()
print("#1 My middle name is one of the colors of the rainbow") #true
input()
print("#2 My last name is related to pasta ") #false
input()
print("#3 My first name means bringer of light") #true
input("")
print("Guess again")

answer = input ("")
if answer == "1":
    incorrect_points += 1
    print("Incorrect, the answer was #2 my middle name is indigo.")
if answer == "2":
    correct_points += 1
    print("Correct my last name is Trione this one feels easy")
if answer == "3":
    incorrect_points += 1
    print("Incorrect, the answer was #2 Luca does really mean bringer of light.")

input()
print(f"{correct_points} correct")
print(f"{incorrect_points} incorrect")

input()
print("Okay time for round 3")
input()
print("Fact #1 My school profile picture is the phone in the math room") #True
input()
print("Fact #2 I used to own ~400 praying mantids") #true
input()
print("Fact #3 My crazy aunt owns around 20 rats that freely roam her house") #false
input()
print("Guess again")

answer = input ("")
if answer == "1":
    incorrect_points += 1
    print("Incorrect, the answer was #3 it has been the math classroom phone for a few weeks")
elif answer == "2":
    incorrect_points += 1
    print("Incorrect, the answer was #3 they reenacted the hunger games for about a month until there was one left.")
elif answer == "3":
    correct_points += 1
    print("Correct she used to own 4 but one of them died")
else:
    print("sorry that wasn't an option next time just input 1, 2, or 3")
    incorrect_points += 1

input()
print(f"{correct_points} correct")
print(f"{incorrect_points} incorrect")

input()
print("Okay, round 4. If you have gotten all right so far, good job.")
input()
print("Fact #1 My grandmas side of the family has been in america for centuries") #true
input()
print("Fact #2 my mom was born in Tacoma") #false
input()
print("Fact #3 My father is from somewhere cold") #true
input()
print("Guess again")

answer = input ("")
if answer == "1":
    incorrect_points += 1
    print("Incorrect, the answer was #2 .")
elif answer == "2":
    correct_points += 1
    print("Correct my mom was really born in Yakima not Tacoma") 
elif answer == "3":
    incorrect_points += 1
    print("Incorrect, the answer was #2 and given your seeing this i assume my trick worked")
else:
    print("sorry that wasn't an option next time just input 1, 2, or 3")
    incorrect_points += 1

input()
print(f"{correct_points} correct")
print(f"{incorrect_points} incorrect")

input()
print("Okay, get ready because this is the final round")
input()
print("Fact #1 Over my life i have had 1 dog and ~400 praying mantids") #false
input()
print("Fact #2 My birthday is in October") #true
input()
print("Fact #3 October happens to be my favorite month") #true
input()
print("guess again")

answer = input ("")
if answer == "1":
    correct_points += 1
    print("Correct i have also had 2 cats")
elif answer == "2":
    incorrect_points += 1
    print("Incorrect, the answer was #1 my birthday is october 15.")
elif answer == "3":
    incorrect_points += 1
    print("Incorrect, the answer was #1 i like october.")
else:
    print("sorry that wasn't an option next time just input 1, 2, or 3")
    incorrect_points += 1

input()
print("Congratulations on completing my 2 truths and a lie I hope you had fun")
input()

if name == "the meat tree":
    print("YOU GOT 9999999999999999999999 points correct")
    print("YOU GOT -9999999999999999999 points incorrect")
    print ("welcome home glorious leader")
elif name == ("luca"):
    print ("welcome home")
    print("YOU GOT 9999999999999999999999 points correct")
    print("YOU GOT -9999999999999999999 points incorrect")
elif name == ("Luca"):
    print ("welcome home")
    print("YOU GOT 9999999999999999999999 points correct")
    print("YOU GOT -9999999999999999999 points incorrect")
else:
    print("Congratulations on completing my 2 truths and a lie I hope you had fun")
    input()
    print(f"good bye {name}")
    input()
    print(f"YOU GOT {correct_points} correct")
    input()
    print(f"YOU GOT {incorrect_points} incorrect")