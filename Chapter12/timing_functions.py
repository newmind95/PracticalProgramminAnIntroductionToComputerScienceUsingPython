import time
import smallest_value
import sort_identify_get_indices


def time_find_two_smallest(find_func, lst):
    """
    (function, list) -> float

    Return how many seconds find_func(lst) took to execute.

    """

    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_counter()
    return (t1 - t2) * 1000.


if __name__ == "__main__":
    sea_levels = []
    sea_levels_file = open('sea_levels.txt', 'r')
    for line in sea_levels_file:
        sea_levels.append(float(line))

    find_remove_find_time = time_find_two_smallest(
        smallest_value.find_two_smallest, sea_levels)

    sort_get_minimums_time = time_find_two_smallest(
        sort_identify_get_indices.find_two_smallest, sea_levels)

    print('"Find, remove, find" took {:.2f}ms.'.format(find_remove_find_time))