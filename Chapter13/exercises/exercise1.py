"""All three versions of linear search start at index 0.
Rewrite all three to search from the end of the list
instead of from the beginning. Make sure you test them."""

def linear_search_v1(lst, value):
    """(list, object) -> int
    Returns the index of the first occurrence in list,
    or return -1 if its not in list.
    
    >>> linear_search([2, 5, 1, -3], 5)
        2
        
    >>> linear_search_v1([2, 5, 1, -3], -3)
        0
    """
    
    for i in range(len(lst)):
        if lst[i-1] == value:
            return i
    return -1


def linear_search_v2(lst, value):
    """(list, object) -> int
    Returns the index of the first occurrence in list,
    or return -1 if its not in list.
    """
    
    # examine every index i in lst, starting from end of lst:
    # Is lst[i] the value we are searching for? If so, stop searching.
    i = 0    # The index of next item in lst to examine
    while i != len(lst) and lst[i-1] != value:
        i -= 1
        
    if i == len(lst):
        return -1
    else:
        return i
    

def linear_search_v3(lst, value):
    """(list, object) -> int
    Returns the index of the first occurrence in list,
    or return -1 if its not in lst.
    """
    
    # examine each item in lst, starting from end of lst:
    # Is the lst[i] the value we are searching for? If so stop searching.
    lst.append(value)
    i = -1   # The index of the next item in lst to examine
    while lst[i-1] != value:
        i -= 1
        
    # Remove the sentinel
    lst.pop()
        
    if i == len(lst):    # The index we are searching is not in lst.
        return -1
    else:
        return i
        
    
print(linear_search_v1([2, 5, 1, -3], -3))
print(linear_search_v1([2, 5, 1, -3], 5))
print(linear_search_v1([2, 5, 2, -4], -4))

print(linear_search_v2([2, 5, 1, -3], -3))
print(linear_search_v2([2, 5, 1, -3], 5))
print(linear_search_v2([2, 5, 2, -4], -4))

print(linear_search_v3([2, 5, 1, -3], -3))
print(linear_search_v3([2, 5, 1, -3], 5))