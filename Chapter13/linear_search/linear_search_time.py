import time
import linear_search_1
import linear_search_2
import linear_search_3


def time_it(search, L, value):
    """ (function, object, list) -> number
    Time how long it takes to run functions search to find
    value v in list L.
    """

    t1 = time.perf_counter()
    search(L, value)
    t2 = time.perf_counter()

    return (t2 - t1) * 1000.0


def print_times(value, L):
    """ (object, list) -> NoneType
    Print the number of milliseconds it takes for linear_search(value, L)
    to run for list.index, the while loop linear_search, the for loop linear search,
    and sentinel search.
    """

    t1 = time.perf_counter()
    L.index(value)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    # Get the other three running times.
    while_time = time_it(linear_search_1.linear_search, L, value)
    for_time = time_it(linear_search_2.linear_search, L, value)
    sentinel_time = time_it(linear_search_3.linear_search, L, value)

    print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(
            value, while_time, for_time, sentinel_time, index_time))


L = list(range(10000001))

print_times(10, L)
print_times(5000000, L)
print_times(10000000, L)
