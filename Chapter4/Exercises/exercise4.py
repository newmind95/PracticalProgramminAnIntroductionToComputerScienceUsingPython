"""
Complete the examples in the docstring and then write the body of the
following function:
def repeat(s, n):
(str, int) -> str
Return s repeated n times; if n is negative, return the empty string.
    repeat('yes', 4)
    'yesyesyesyes'
    repeat('no', 0)

    repeat('no', -2)

    repeat('yesnomaybe', 3)

"""


def repeat(s, n):
    """
    (str, int) -> str

    Returns repeated n times; if n is negative return the empty string.
    """
    if n > 0:
        return s * n
    else:
        return ''


print(repeat('yes', 4))
print(repeat('no', 0))
print(repeat('no', -2))
print(repeat('yesnomaybe', 3))
