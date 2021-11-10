"""
A balanced color is one whose red, green, and blue values add up to 1.0.
Write a function called is_balanced that takes a dictionary whose keys are
'R' , 'G' , and 'B' and whose values are between 0 and 1 as input and returns
True if they represent a balanced color.
"""


def is_balanced(xdict):

    for key, value in xdict.items():
        if value in xdict.values():
            if value == 0:
                value += 1
                return True
            else:
                return False


xdict = {'R': 0, 'G': 0, 'B': 1}
print(is_balanced(xdict))
