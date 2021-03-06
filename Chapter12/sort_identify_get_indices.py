def find_two_smallest(L):
    """
    (list of float) -> tuple of (int, int)

    Return a tuple of the indices of the two smallest values in list L.

    find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """

    # Get a sorted copy of the list so that the smallest items
    # are at the front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # Find the two smallest indices
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)

    # Return the two smallest indices
    return min1, min2


print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))
