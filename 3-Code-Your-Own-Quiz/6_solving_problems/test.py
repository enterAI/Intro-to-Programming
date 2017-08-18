# IPND Stage 2 Final Project

# Version : Python 3
# The objective of this game is to match 3 heroes of Avengers. The script source is here.
# https://geektyrant.com/news/2011/11/30/the-avengers-official-character-descriptions-released.html

# Parts Of Speech
parts_of_speech  = ["__1__", "__2__", "__3__"]

# The following are strings to pass in to the play_game function.
ml_string = [
 "On top of being an eccentric genius, a billionaire, a playboy and a philanthropist, Tony Stark (Robert Downey Jr.) is also the armored super hero known as __1__. Fresh off of defeating enemies the world over, Stark reluctantly agreed to serve as a consultant to Nick Fury’s top-secret peacekeeping and intelligence agency known as S.H.I.E.L.D. Now, with a global crisis on the horizon and the fate of the world in the balance, Stark must again power up his __1__ armor to save the world, and become a full-fledged member of The Avengers.",
 "An arrogant prince from the distant land of Asgard, __2__ (Chris Hemsworth) was banished to Earth after his irresponsible behavior threatened his homeland. While in exile on Earth, __2__ learned humility and helped to save his new friends from a destructive threat sent by his brother Loki. In the process, __2__ redeemed himself in the eyes of his father, Odin, the King of Asgard. After being welcomed back to Asgard as a hero, __2__ must now return to Earth once again to prevent a cosmic-level catastrophe. With Mjolnir in his hand, a legendary hammer with immense power, the mighty warrior soon finds himself drawn into an unlikely alliance with Nick Fury’s secret initiative, The Avengers, lending his power to their cause against his wayward brother, Loki.",
 "One of S.H.I.E.L.D.’s most elite agents, Clint Barton (Jeremy Renner), code-named __3__, is the greatest living marksman on Earth. Armed with his weapon of choice, the recurve bow, __3__ fires his arsenal of custom augmented arrows, specialized for any number of specific situations, with perfect precision. With the potential for global catastrophe on the horizon, he employs his amazing combat skills to fight along side The Avengers."
 ]

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech, i):
    replaced = []
    ml_string_splited = ""
    ml_string_splited = ml_string[i].split()
    user_input = ""
    print ("")
    print ("No. {} Quiz: What is the name of this hero in the Avengers?: __{}__".format(i+1, i+1))
    print ("")
    print (ml_string[i])
    for word in ml_string_splited:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            #########################
            # I add this condition to solve the problems by only fitting 'once'.
            #########################
            if user_input != "":
                word = word.replace(replacement, user_input)
                replaced.append(word)
            else:
                user_input = input("Type in a " + replacement + ": ")
                word = word.replace(replacement, user_input)
                replaced.append(word)
        else:
            replaced.append(word)
    print ("")
    print ("You just finished the NO." + str(i+1) + " Quiz. The result is ..: ")
    print ("")

    if i == 0:
        #########################
        # I have made many examples to predict user's answers.
        # There seems to be an easier way, but I'm not sure.
        #########################
        if (user_input != "Iron Man" and user_input != "ironman" and user_input != "Iron_Man"
        and user_input != "Ironman" and user_input != "Iron_man" and user_input != "iron_man"
        and user_input != "iron_man" and user_input != "iron man"):
            print ("That isn't the correct answer!")
            return False
        else:
            print ("Congratulations! You have passed the first quiz!!")
            print ("")
            print ("The original text is: ")

    if i == 1:
        if user_input != "Thor" and user_input != "thor":
            print ("That isn't the correct answer!")
            return False
        else:
            print ("Congratulations! You have passed the second quiz!!")
            print ("")
            print ("The original text is: ")

    if i == 2:
        if (user_input != "HawkEye" and user_input != "Hawkeye" and user_input != "hawkeye"
        and user_input != "Hawk_eye" and user_input != "Hawk_Eye"):
            print ("That isn't the correct answer!")
            return False
        else:
            print ("Congratulations! You have passed the last quiz!!")
            print ("")
            print ("The original text is: ")

    replaced = " ".join(replaced)
    return replaced

#########################
# This is the code that actually runs the game.
# This code iterates ml_string and counts the wrong answers.
#########################
count = 0
count_false = 0
print("Guess three Heroes!")
while count < len(ml_string):
    result = play_game(ml_string, parts_of_speech, count)
    print(result)
    if result == False:
        count_false += 1
    count += 1
if count_false == 0 :
    print ("")
    print ("Wow! You are a fan of the Avengers!")
    print ("")
else:
    print ("")
    print ("{} of the 3 heros are incorrect. Your are not a fan of the Avengers.. :(".format(count_false))
    print ("")
