def linear_search(L, value):
    """
    (list, object) -> int

    Return the index of the first occurrence of value in list,
    or return -1 if value is not in list.

    linear_search([2, 5, 1, -3], 5)
    1

    linear_search([2, 4, 2], 2)
    0

    linear_search([2, 5, 1, -3], 4)
    -1
    """

    # examine at each index i in list, starting at index 0:
    # is L[i] the value we are looking for? if so, stop searching.

    i = 0       # The index of the next item in L to examine.

    # Keep going until we reach the end of L or until we find value.
    while i != len(L) and L[i] != value:
        i += 1

    # If we fell off the end of the list, we did not find the value.
    if i == len(L):
        return -1
    else:
        return i


#print(linear_search([2, 5, 1, -3], 5))
#print(linear_search([2, 5, 1, -3], 4))
