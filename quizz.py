science_points = 0
history_points = 0
geography_points = 0

name = input("Hello there what is your name")
answer_0 = input (f"Hello {name} are you ready to play Who Wants to Have a Million USD tm. if so just say yes ")
if answer_0 == "yes" or answer_0 == "yes":
    print ("Thats great time to play")
    input ()
    print ("Okay question 1 when was seattle founded")
    print ("A: 1832")
    print ("B: 1911")
    print ("C: 1851")
    answer_1 = input ("Or D: 1874. just say A, B, C, or D ")
    if answer_1 == "C" or answer_1 == "c":
        print ("That is correct good job")
        history_points += 1
    else:
        print (f"Wrong it was C not {answer_1}")
        history_points -= 1
    
    print ("Okay time for question 2")
    answer_2 = input ("This one is not multiple choice what is the largest country, remember to capitalize: ")
    if answer_2 == "Russia":
        print ("That is correct good job")
        geography_points += 1
    else:
        print (f"Incorrect it was Russia not {answer_2}")
        geography_points -= 1
    
    print ("okay question 3")
    input ()
    print ("How many elements are on the periodic table: ")
    print ("A: 118")
    print ("B: 82")
    print ("C: infinite the school one just shows the stable ones")
    print ("D: there is disagreement and we")
    answer_3 = input ("so is it A, B, C, or D")
    if answer_3 == "A" or answer_3 == "a":
        print ("correct there are 118")
        science_points += 1
    else:
        print (f"wrong it was A 118 not {answer_3}")
        science_points -= 1


    if answer_3 == "118":
        print ("good job")

else:
    print ("       oh ... okay ... bye then")