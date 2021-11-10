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

    for i in range(len(L)):

        if L[i] == value:
            return i

    return -1


print(linear_search([2, 5, 1, -3], 4))
