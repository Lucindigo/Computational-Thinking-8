science_points = 0
history_points = 0
geography_points = 0

name = input("Hello there what is your name ")
answer_0 = input (f"Hello {name} are you ready to play Who Wants to Have a Million USD tm. if so just say yes ")
if answer_0 == "yes" or answer_0 == "Yes":
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

    input ()
    print ("Okay time for question 2")
    input ()
    answer_2 = input ("This one is not multiple choice what is the largest country, remember to capitalize: ")
    if answer_2 == "Russia":
        print ("That is correct good job")
        geography_points += 1
    else:
        print (f"Incorrect it was Russia not {answer_2}")
        geography_points -= 1
    
    input ()
    print ("okay question 3")
    input ()
    print ("How many elements are on the periodic table: ")
    print ("A: 118")
    print ("B: 82")
    print ("C: infinite the more known one only shows the stable ones")
    print ("D: there is disagreement and we dont know")
    answer_3 = input ("so is it A, B, C, or D: ")
    if answer_3 == "A" or answer_3 == "a":
        print ("correct there are 118")
        science_points += 1
    else:
        print (f"wrong it was A 118 not {answer_3}")
        science_points -= 1
    
    input ()
    answer_4 = input ("okay question 4 when was america founded: ")
    if answer_4 == "1776":
        print ("correct you did it")
        history_points += 1
    else:
        print (f"it was 1776 not {answer_4}")
        history_points -= 1
    
    input ()
    print ("time for #5")
    input ()
    answer_5 = input ("this is a more objective question so multiple answers are correct but anyways. how many countries are there: ")
    if answer_5 == "193" or answer_5 == "195" or answer_5 == "197" or answer_5 == "204":
        print ("your answer was correct according to UN member states, the UN, the UN plus some, or the olympics")
        geography_points += 1
    else:
        print ("Sorry you were probably wrong but this was an objective question")
        geography_points -= 1
    
    input ()
    print ("okay question 6 this is multiple choice but i had a bit of fun so feel free to just type the answer if you know it")
    input ()
    print ("how old is the universe rounded to the nearest 10 million years")
    print ("A: 1.00 billion years")
    print ("B: 1.28 billion years")
    print ("C: 1.97 billion years")
    print ("D: 2.77 billion years")
    print ("E: 3.44 billion years")
    print ("F: 4.82 billion years")
    print ("G: 5.51 billion years")
    print ("H: 6.81 billion years")
    print ("I: 7.16 billion years")
    print ("J: 7.36 billion years")
    print ("K: 7.82 billion years")
    print ("L: 9.42 billion years")
    print ("M: 11.72 billion years")
    print ("N: 13.80 billion years")
    print ("O: 18.54 billion years")
    print ("P: 44.21 billion years")
    print ("Q: infinitely old")
    print ("R: nobody knows")
    answer_6 = input ("So... what is it: ")
    if answer_6 == "N" or answer_6 == "13.8 billion years" or answer_6 == "13.80 billion years" or answer_6 == "13.8" or answer_6 == "13.80":
        print ("Yay you did it")
        science_points += 1
    else:
        print (f"incorrect it was N or 13.8 billion years not {answer_6}")
        science_points -= 1
    
    input ()
    print ("okay time for #7")
    input ()
    answer_7 = input ("what is the worlds oldest country remember to capitalize: ")
    if answer_7 == "China" or answer_7 == "Egypt" or answer_7 == "Iran":
        print ("Yay you did it")
        history_points += 1
    else:
        print ("you did not get it right")
        history_points -= 1
    
    input ()
    print ("okay time for the penultimate question")
    input ()
    answer_7 = input ("what is the name of the line splitting America and Canada")
    if answer_7 == "49th parallel" or answer_7 == "the 49th parallel":
        print ("Yay you did it")
        geography_points += 1
    else:
        print ("no and if you said a a border im disappointed")
        geography_points -= 1

    print ("okay final question")
    input ()
    print ("~how many AU are between the earth and the sun")
    print ("A: ~0.00006")
    print ("B: ~0.03441")
    print ("C: ~0.01223")
    print ("D: ~0.23441")
    print ("E: ~0.27")
    print ("F: ~0.891")
    print ("G: ~1")
    print ("H: ~0.552")
    print ("I: 0.324")
    print ("J: an AU the 1/100 the distance between the earth and the sun so its 100")
    answer_9 = input ("soooo... i had fun again you can just type it if you dont want to read that")
    if answer_9 == "1" or answer_9 == "G":
        print ("Yay you did it time to see your results")
        science_points += 1
    else:
        print ("sorry but no")
        science_points -= 1
    
    print ("okay time for you to see what you are best at")
    input ()
    if science_points > history_points and science_points > geography_points:
        print (f"you are a science person getting {science_points}/3 science questions correct")
    elif history_points > science_points and history_points > geography_points:
        print (f"you are a history person getting {history_points}/3 history questions correct")
    elif geography_points > science_points and geography_points > history_points:
        print (f"you are a geography person getting {geography_points}/3 geography questions correct")
    elif geography_points == 3 and history_points == 3 and science_points == 3:
        print ("you are too smart i cant grade you")
        input ()
        print ("unless you used Google then you are not smart and disregard any previous praise")
    else:
        print ("you tied in some way but didn't get 3 in all of them")
        print (f"you got {science_points}/3 science questions correct")
        print (f"you got {history_points}/3 history questions right")
        print (f"and you got {geography_points}/3 geography questions")

else:
    print ("       oh ... okay ... bye then")
    input ()
    input ()
    input ()
    input ()
    input ()
    input ()
    print ("kind of rude")