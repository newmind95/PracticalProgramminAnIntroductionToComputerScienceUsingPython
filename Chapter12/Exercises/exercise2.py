"""
In this exercise, you’ll develop a function that finds the minimum or
maximum value in a list, depending on the caller’s request.
"""

"""
a. Write a loop (including initialization) to find both the minimum value
in a list and that value’s index in one pass through the list.
"""

L = [242, 22, 32, 24, 52, 523]

smallest_value = min(L)
smallest_index = L.index(smallest_value)

for i in L:

    if i < smallest_value:
        smallest_value = i

    if i < smallest_index:
        smallest_index += 1

print (smallest_value, smallest_index)

"""
b.Write a function named min_index that takes one parameter (a list ) and
returns a tuple containing the minimum value in the list and that
value’s index in the list.
"""


def min_index(L):

    value = min(L)
    index = L.index(value)

    for i in L:

        if i < value:
            value = i

        if i < index:
            index += 1

    return value, index


print(min_index(L))


"""
c.You might also want to find the maximum value and its index. Write
a function named min_or_max_index that has two parameters: a list and
a bool . If the Boolean parameter refers to True , the function returns a
tuple containing the minimum and its index; and if it refers to False ,
it returns a tuple containing the maximum and its index.
"""


def min_or_max_index(L, flag):

    min_value = min(L)
    max_value = max(L)

    min_index_value = L.index(min_value)
    max_index_value = L.index(max_value)

    for i in L:

        if flag:
            if i < min_value:
                min_value = i

            if i < min_index_value:
                min_index_value += 1

            return min_value, min_index_value

        elif not flag:

            if i > max_value:
                max_value = i

            if i > max_index_value:
                max_index_value += 1

            return max_value, max_index_value


print(min_or_max_index(L, False))
