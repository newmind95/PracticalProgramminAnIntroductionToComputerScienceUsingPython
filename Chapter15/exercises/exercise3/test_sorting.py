import unittest

"""
Using unittest , write the five most informative tests you can think of for a
function called is_sorted in a module called TestSorting.py that takes a list of
integers as input and returns True if they are sorted in nondecreasing
order (as opposed to strictly increasing order, because of the possibility
of duplicate values), and False otherwise.
"""


def is_sorted(lst):
    i = 0
    n = len(lst)
    already_sorted = True
    while i != len(lst):
        j = 0
        while j < n-1:
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                already_sorted = False
            j += 1
        if not already_sorted:
            break
        i += 1
    return already_sorted


class TestSorting(unittest.TestCase):
    """Test is_sorted()."""


    def test_empty(self):
        argument = is_sorted([])
        expected = True
        self.assertEqual(argument, expected,
                         'Test with empty list.')


    def test_one_element(self):
        argument = is_sorted([1])
        expected = True
        self.assertEqual(argument, expected,
                         'Test with one element.')


    def test_multiple_elements_already_sorted(self):
        argument = is_sorted([1, 1, 3, 3, 4, 4, 5, 10])
        expected = True
        self.assertEqual(argument, expected,
                         'Test with multiple elements.')


    def test_negative_elements(self):
        argument = is_sorted([1, -1, -2, 3])
        expected = False
        self.assertEqual(argument, expected,
                         'Test with negative elements.')


unittest.main()
