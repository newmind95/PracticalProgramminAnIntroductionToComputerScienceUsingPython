"""
Complete the examples in the docstring and then write the body of the
following function:
def total_occurrences(s1, s2, ch):
 (str, str, str) -> int
Precondition: len(ch) == 1
Return the total number of times that ch occurs in s1 and s2.
total_occurrences('color', 'yellow', 'l')
3
total_occurrences('red', 'blue', 'l')

total_occurrences('green', 'purple', 'b')

"""


def total_occurrences(s1, s2, ch):
    """

    (str, str, str) -> int
    """
    if len(ch) == 1:
        return s2.find(ch, s1.find(ch) + 1)
    else:
        raise Exception('Length of character must be 1')


print(total_occurrences('color', 'yellow', 'l'))
print(total_occurrences('red', 'blue', 'l'))
print(total_occurrences('green', 'purple', 'b'))
