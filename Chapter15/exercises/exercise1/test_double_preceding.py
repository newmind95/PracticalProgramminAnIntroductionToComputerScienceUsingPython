import unittest
import double_preceding as dp


class TestDoublePreceding(unittest.TestCase):
    """Test double preceding."""


    def test_double_preceding_empty(self):
        """Test a empty list."""
        argument = []
        expected = []
        dp.double_preceding(argument)
        self.assertEqual(expected, argument,
                         'Test a empty list.')


    def test_double_preceding_one_item(self):
        """Test a one-item list."""
        argument = [5]
        expected = [0]
        dp.double_preceding(argument)
        self.assertEqual(expected, argument,
                         'Test a one-item list.')


    def test_double_preceding_two_items(self):
        """Test a two-item list."""
        argument = [5, 7]
        expected = [0, 10]
        dp.double_preceding(argument)
        self.assertEqual(expected, argument,
                         'Test a two-item list.')


    def test_double_preceding_negative(self):
        """Test negative values in the list."""
        argument = [-1, -3, -4, -5]
        expected = [0, -2, -6, -8]
        dp.double_preceding(argument)
        self.assertEqual(expected, argument,
                         'Test a list of negative values.')


    def test_double_preceding_positive(self):
        """Test positive values in the list."""
        argument = [3, 5, 7, 10, 11]
        expected = [0, 6, 10, 14, 20]
        dp.double_preceding(argument)
        self.assertEqual(expected, argument,
                         'Test positive values in the list.')

unittest.main()
