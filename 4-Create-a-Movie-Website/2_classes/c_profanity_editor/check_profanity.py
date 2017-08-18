# Lesson 3.3: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarassing! Imagine how you'd feel if you
# accidentally sent your boss an email that said "I'll take
# a sh!t at it" instead of "I'll take a shot at it". Write
# a program that can detect curse words in a string of text.

# Use this space to describe your approach to the problem.
#
#
#
#

import urllib.request

def read_text():
    # Your code here.
    quotes = open("/Users/choi/Desktop/ipnd/4-Create-a-Movie-Website/2_classes/c_profanity_editor/movie_quotes.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()

def check_profanity(text):
    # Your code here.
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    if str.encode("true") in output:
        print("Profanity Alert!!")
    elif str.encode("false") in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    connection.close()



#read_text()
check_profanity(" ")
