# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4152219158/concepts/50376191640923

p = ['y', 'a', 'b', 'b', 'a', '!']
print (p)
print (p[0])
print (p[2:4])

# Add your own code and notes here
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print (list_with_lists[2][0:2])

s = "hello"
s += " 3"
s += str(10)
l = ["h", "e", "l", "l", "o"]
l[0] = "y"
l += [3]
l[2] = '!'
print (l)
print (s)

spy = [0,0,7]
spy = spy + [1]
spy.append("1")
print (spy)
spy2 = [1,1,2]
print(len(spy))
