"""
Given variables x and y , which refer to values 3 and 12.5 , respectively, use
function print to print the following messages. When numbers appear in
the messages, variables x and y should be used.

a.  The rabbit is 3.
b.  The rabbit is 3 years old.
c.  12.5 is average.
d.  12.5 * 3
e.  12.5 * 3 is 37.5.
"""

x = 3
y = 12.5

print("a. The rabbit is", x)
print("b. The rabbit is", x, end=' years old.\n')
print("c. ", y, end=' is average.\n')
print("d. ", y, " * ", x)
print("e. ", y, " * ", x, " is ", y * x)
