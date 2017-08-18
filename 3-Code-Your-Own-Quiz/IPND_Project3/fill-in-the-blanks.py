# IPND Stage 3 Final Project

# Created by Wonseok, Choi
# Version : Python 3

# Parts Of Speech
parts_of_speech  = ["__1__", "__2__", "__3__", "__4__", "__5__"]

# The following are strings and answer sheet to pass in to the play_game function.
game_data = {
   'easy': {
        'quiz': "Math Quiz: \n1. 9 - 6 = __1__ \n2. 16 * 3 = __2__ \n3. ln(e) = __3__, \n4. What is the missing number from the following sequence: 8, 16, 32, ...,128, 256, 512? answer: __4__",
        'answers': ["3","48","1","64"],
        'num_problems': 4
    },
   'medium': {
        'quiz': "Syntax of Python: \n The __1__ statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if). \n The __2__ statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block. \n The __3__ statement, which executes a block of code as long as its condition is true. \n The __4__ statement, which is used to __4__ modules whose functions or variables can be used in the current program. \n The __5__ statement was changed to the __5__() function in Python 3",
        'answers': ["if", "for", "while", "import", "print"],
        'num_problems': 5
    },
   'hard': {
        'quiz': " __1__ all my troubles seemed so far __3__.\n  __4__ it looks as though they're here to stay.\n       __2__, I believe in __1__.\n\n Suddenly I'm not half the man I used to be.\n    There's a shadow hanging over me.\n       __2__, __1__ came suddenly.\n\nWhy she had to go, I don't know, she wouldn't say.\n I said something wrong, __4__ I long for __1__.\n\n __1__ love was such an easy game to play.\n    __4__ I need a place to hide __3__.\n       __2__, I believe in __1__.\n\nWhy she had to go, I don't know, she wouldn't say.\n I said something wrong, __4__ I long for __1__.\n\n __1__ love was such an easy game to play.\n     __4__ I need a place to hide __3__.\n        __2__, I believe in __1__.",
        'answers': ["yesterday", "away", "now", "oh"],
        'num_problems': 4
    }
}
# Fine matched word function
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Return false count
def false_counter(false_count, total_try_number):
    """
    Args:
        false_count: count the user's answer if false.
        total_try_number: total chance users have.
    Behavior:
        Count the user's answer if false, and print out how many chances they have.
    Returns:
        Number of trials.
    """
    false_count += 1
    # This condition exists for the last attempt, i.e. to do not print "you got 0 left"
    if total_try_number != false_count:
        print ("you are wrong... you have {} chances in total".format(total_try_number - false_count))
    else: # if every trial got wrong, get out
        print ("You failed the game. \nExit Python.")
        exit()
    return false_count

# Return problem count
def correct_message_with_problem_counter(ml_string, num_problem):
    """
    Args:
        ml_string: show text with correct answers which user solve.
        num_problem: number of problem which user should solve next.
    Behavior:
        Print out the text with correct answers which user solve and the 'Correct!' message.
    Returns:
        Number of problem they should solve.
    """
    print ("")
    print ("**Correct!**")
    print (ml_string)
    num_problem += 1
    return num_problem

# This function split the 'updated' ml_string_splited into word
def match_answer(ml_string_splited, false_count, answer_sheet, num_problem, ml_string, num_problems, total_try_number):
    """
    Args:
        ml_string_splited: converted text, i.e. string into text.
        false_count: count the user's answer if false.
        answer_sheet: comparison between answer and user's input.
        num_problem: number of problem which user should solve next.
        ml_string: show text with correct answers which user solve.
        num_problems: number of total problems for each game data.
        total_try_number: total chance users have.
    Behavior:
        Merge the above functions 1)to show text with correct answers which user solve,
                                  2)to count the user's answer if false, and print out how many chances they have.
    Returns:
        Return updated text with correct answers and the next problem.
    """
    for word in ml_string_splited:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            print ("")
            user_input = input("Type in a " + replacement + ": ")
            if user_input != answer_sheet[num_problem]:
                false_count = false_counter(false_count, total_try_number)
                break
            else:
                ml_string = ml_string.replace(replacement, user_input)
                ml_string_splited = ml_string.split()
                # This condition exists for the last attempt, i.e. to do not reprint any correct text.
                if num_problem < num_problems - 1:
                    num_problem = correct_message_with_problem_counter(ml_string, num_problem)
                break
    return ml_string, ml_string_splited, num_problem, false_count

# Merged every function and print statement
def play_game(ml_string, answer_sheet, num_problems):
    """
    Args:
        ml_string: show text which user should solve.
        answer_sheet: comparison between answer and user's input.
        num_problems: number of total problems for each game data.
    Behavior:
        Merge every functions to play the game with messages.
    Returns:
        Return the complete, correct text.
    """
    num_problem = 0
    total_try_number = 5
    false_count = 0
    replaced = []
    ml_string_splited = ml_string.split()
    user_input = ""
    print ("**************************")
    print (ml_string)
    # When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
    for count in ml_string_splited:
        ml_string, ml_string_splited, num_problem, false_count = match_answer(ml_string_splited, false_count, answer_sheet, num_problem, ml_string, num_problems, total_try_number)
    print ("")
    print ("*****************************************************")
    print ("Congratulations! You win the game!")
    return ml_string

# This code selects the game data, i.e. string and answer sheet for each level.
print ("Please enter a Level with only lowercase letters.")
print ("1. easy:     Math Quiz \n2. medium:   Python Syntax Quiz\n3. hard:     Some Famous Lyrics")
type_value = False
while type_value != True:
    user_level = input("Select a Lavel: ")
    # To prevent key error.
    if user_level not in game_data:
        print ("Please enter only lowercase letters.")
    # select the game data with dictionary.
    else:
        text = game_data[user_level]['quiz']
        answer_sheet = game_data[user_level]['answers']
        num_problems = game_data[user_level]['num_problems']
        type_value = True
        print ("\nGreat! you choose {} level. Cheers!".format(user_level))

# Play the game!
print (play_game(text, answer_sheet, num_problems))
