"""
Complete the examples in the docstring and then write the body of the
following function:
    def total_length(s1, s2):
     (str, str) -> int
 Return the sum of the lengths of s1 and s2.
     total_length('yes', 'no')
     5

    total_length('yes', '')
    3

    total_length('YES!!!!', 'Noooooo')
    14

"""


def total_length(s1, s2):
    """
    (str, str) -> int

    Return the sum of the lengths of s1 and s2.
    """
    return len(s1) + len(s2)


print(total_length('yes', 'no'))
print(total_length('yes', ''))
print(total_length('YES!!!!', 'Noooooo'))
