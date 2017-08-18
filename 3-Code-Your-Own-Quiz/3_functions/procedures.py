# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4141089439/concepts/50282994840923

def rest_of_string(s):
    return s[1:]

print (rest_of_string('audacity'))

# Add your own code and notes here
s = ''
print (('a' + s)[1:])
#print (s[0] + s[1:])
print (s + '')
print (s[0:])

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""

#noun_position = #fill this in
#verb_position = #fill this in
text.find("NOUN")
new = text.replace(text[0], "I")
print (new)
