import time
import random
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort

def built_in(L):
    """(list) -> NoneType

    Call list.sort --- we need our own function to do this so that
    we can treat it as we treat our own sorts.
    """
    L.sort()
    
def print_times(L):
    """(list) -> NoneType
    Print the number of milliseconds it takes for selection sort,
    insertion sort, and list.sort to run.
    """
    print(len(L), end='\t')
    for func in (selection_sort, insertion_sort, built_in, bubble_sort):
        if func in (selection_sort, insertion_sort, bubble_sort) and len(L) > 10000:
            continue
        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print(f'{((t2-t1)*1000):.2f}', end='\t')
    print()

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)