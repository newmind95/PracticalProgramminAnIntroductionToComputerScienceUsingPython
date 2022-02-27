def find_min(L, b):
    """(list, int) -> int
    Precondition: if L[b:] is not empty
    Return the index of the smallest value in L[b:].
    """
    smallest = b     # The smallest value seen so far
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            smallest = i
        i+=1
    return smallest

def selection_sort(L):
    """ list -> NoneType
    Reorder the items from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]

    >>> L = [3, 3, 3]
    >>> selection_sort(L)
    >>> L
    [3, 3, 3]

    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> selection_sort(L)
    >>> L
    [-6, -5, 3, 0, 3, -6, 2, 1, 1]

    >>> L = [-2, 1, 4, 6, 7, 8, 9, 11]
    >>> selection_sort(L)
    >>> L
    [-2, 1, 4, 6, 7, 8, 9, 11]
    """
    i = 0    # The index of the unknow item in lst[i:]
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i += 1
    return smallest