"""
The keys in a dictionary are guaranteed to be unique, but the values are
not. Write a function called count_values that takes a single dictionary as
an argument and returns the number of distinct values it contains. Given
the input {'red': 1, 'green': 1, 'blue': 2} , for example, it should return 2 .
"""


def count_values(xdict):

    count = 0

    for key, value in xdict.items():
        if value in xdict.values():
            if value == 1:
                count = count + 1

    return count


xdict = {'red': 1, 'green': 1, 'blue': 2}
print('Number of distinct values: ', count_values(xdict))
