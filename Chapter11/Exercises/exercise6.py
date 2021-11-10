"""
A sparse vector is a vector whose entries are almost all zero, like [1, 0, 0, 0,
0, 0, 3, 0, 0, 0] . Storing all those zeros in a list wastes memory, so program-
mers often use dictionaries instead to keep track of just the nonzero
entries. For example, the vector shown earlier would be represented as
{0:1, 6:3} , because the vector it is meant to represent has the value 1 at
index 0 and the value 3 at index 6.
"""

"""
The sum of two vectors is just the element-wise sum of their elements.
For example, the sum of [1, 2, 3] and [4, 5, 6] is [5, 7, 9] . Write a function
called sparse_add that takes two sparse vectors stored as dictionaries
and returns a new dictionary representing their sum.
"""

def sparse_add(vector1, vector2):

    value = []

    for key1, value1 in vector1.items():
        for key2, value2 in vector2.items():

            if (value1 != 0) and (value2 != 0):
                value.append(value1)

    return dict(value)


print(sparse_add({0: 1, 1: 2, 2: 3}, {0: 4, 1: 5, 2: 6}))
