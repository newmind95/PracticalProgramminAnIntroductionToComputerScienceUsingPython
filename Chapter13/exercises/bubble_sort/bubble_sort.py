def bubble_sort(L):
    """(list) -> NoneType
    Returns the sorted list by traversing, pairs of elements
    are compared, and larger elements are swapped into
    the higher position.
    
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bubble_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]

    >>> L = [3, 3, 3]
    >>> bubble_sort(L)
    >>> L
    [3, 3, 3]

    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> bubble_sort(L)
    >>> L
    [-6, -5, 3, 0, 3, -6, 2, 1, 1]

    >>> L = [-2, 1, 4, 6, 7, 8, 9, 11]
    >>> bubble_sort(L)
    >>> L
    [-2, 1, 4, 6, 7, 8, 9, 11]
    """
    
    # The index of the next item to searching for
    i = 0
    n = len(L)
    while i != len(L):
        already_sorted = False
        j = 0
        while j < n-1:
            # Pairs of elements are compared
            if L[j+1] < L[j]:
                # Larger elements are swapped into the higher position. 
                L[j], L[j+1] = L[j+1], L[j]
                already_sorted = True
            j += 1
            
        if not already_sorted:
            break
        i += 1

L = [3, 4, 7, -1, 2, 5]
bubble_sort(L)
print(L)

L = [3, 3, 3]
bubble_sort(L)
print(L)

L = [-5, 3, 0, 3, -6, 2, 1, 1]
bubble_sort(L)
print(L)

L = [-2, 1, 4, 6, 7, 8, 9, 11]
bubble_sort(L)
print(L)