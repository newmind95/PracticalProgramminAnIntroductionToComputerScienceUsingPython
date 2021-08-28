"""

Complete the examples in the docstring and then write the body of the
following function:
def same_first_last(L):
 (list) -> bool
Precondition: len(L) >= 2

Return True if and only if first item of the list is the same as the
last.

same_first_last([3, 4, 2, 8, 3])
True

same_first_last(['apple', 'banana', 'pear'])

same_first_last([4.0, 4.5])

"""


def same_first_last(L):
    """
    (list) -> bool

    Return True if and only if first item of the list
    is the same as the last.
    """

    if len(L) >= 2:
        if L[0] == L[-1]:
            return True
        else:
            return False


print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(['apple', 'banana', 'pear']))
print(same_first_last([4.0, 4.5]))
print(same_first_last([4.0, 4.5, 4.0]))