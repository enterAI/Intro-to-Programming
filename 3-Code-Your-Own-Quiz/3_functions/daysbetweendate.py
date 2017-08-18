# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    daysOfyears = (y1 - y2) * sum(daysOfMonths)
    if m1 == 1:
        daysOfmonth_today = 0
    else:
        daysOfmonth_today = sum(daysOfMonths[:m1-1])
    if m2 == 1:
        daysOfmonth_birthday = 0
    else:
        daysOfmonth_birthday = sum(daysOfMonths[:m2-1])
    daysOfmonth = daysOfmonth_today - daysOfmonth_birthday
    days = daysOfyears + daysOfmonth + (d1 - d2)
    return days

print (daysBetweenDates(2017, 5, 1, 1990, 5, 6))
