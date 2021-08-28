"""
In the following exercises, you will work with Python’s calendar module:
a. Visit the Python documentation website at http://docs.python.org/release/
3.3.0/py-modindex.html , and look at the documentation on module calendar .
b. Import module calendar .
c. Using function help , read the description of function isleap .
d. Use isleap to determine the next leap year.
e. Use dir to get a list of what calendar contains.
f. Find and use a function in module calendar to determine how many
leap years there will be between the years 2000 and 2050, inclusive.
g. Find and use a function in module calendar to determine which day of
the week July 29, 2016, will be.
"""

import calendar

print(help(calendar.isleap))


def check_leap(year):
    if calendar.isleap(year):
        return True
    else:
        return False


print(check_leap(2006))
print(check_leap(2020))

print(dir(calendar))

print(calendar.leapdays(2000, 2050))

print(calendar.weekday(2016, 7, 29))
