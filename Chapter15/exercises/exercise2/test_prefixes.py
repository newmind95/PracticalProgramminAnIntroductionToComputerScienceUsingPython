import unittest

"""
Using unittest , write four tests for a function called all_prefixes in a module
called TestPrefixes.py that takes a string as its input and returns the set of
all nonempty substrings that start with the first character. For example,
given the string "lead" as input, all_prefixes would return
the set {"l", "le", "lea", "lead"} .
"""

def all_prefixes(s):
    prefix = ''
    prefix_as_set = set()
    for i in range(len(s)):
        prefix = s[:i+1]
        prefix_as_set.add(prefix)
    return prefix_as_set


class TestPrefixes(unittest.TestCase):
    """Test all_prefixes()"""


    def test_prefixes_empty(self):
        """Test all_prefixes() with empty set."""
        argument = all_prefixes('')
        expected = set()
        self.assertEqual(argument, expected,
                         'Test method all_prefixes with empty string.')

    def test_prefixes_one_letter(self):
        """Test all_prefixes() with one letter."""
        argument = all_prefixes('x')
        expected = {'x'}
        self.assertEqual(argument, expected,
                         'Test method all_prefixes with one letter.')


    def test_prefixes_unique_word(self):
        """Test all_prefixes() with unieque word."""
        argument = all_prefixes('champion')
        expected = {'c', 'ch', 'cha', 'cham', 'champ', 'champi',
                    'champio', 'champion'}
        self.assertEqual(argument, expected,
                         'Test method all_prefixes with unique word.')


    def test_prefixes_multiple(self):
        """Test a word with multiple occurrences of the first letter."""
        argument = 'puppet'
        expected = {'p', 'pu', 'pup', 'pupp', 'puppe', 'puppet', 'pp',
                    'ppe', 'ppet', 'pe', 'pet'}
        self.assertEqual(argument, expected,
                         'Test first letter occurs multiple times.')
        


unittest.main()
