def insert(L, b):
    """(list, int) -> NoneType
    Precondition: L[0:b] is already sorted
    Insert L[b] where it belongs in L[0:b+1]

    >>> L = 3, 4, 7, -1, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    # Find where to insert L[b] by searching backwards from L[b]
    # for a smaller value.
    i = b
    while i != 0 and L[i-1] >= L[b]:
        i-=1
    # Move L[b] to index i, shifting the following values to right.
    value = L[b]
    del L[b]
    L.insert(i, value)


def insertion_sort(L):
    """(list) -> NoneType
    Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        insert(L, i)
        i = i + 1