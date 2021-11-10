def find_two_smallest(L):
    """
    (list of float) -> tuple of (int, int)
    """

    # Find the index of the smallest value in L
    smallest = min(L)
    min1 = L.index(smallest)

    # Remove that value
    L.remove(smallest)

    # Find the second smallest index in L
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # Put the smallest value back in the L
    L.insert(min1, min2)

    # If necessary, adjust the two values
    if min1 <= min2:
        min2 = min2 + 1

    # Return the two smallest values
    return min1, min2


print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))
