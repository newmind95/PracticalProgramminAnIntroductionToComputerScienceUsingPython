"""
Create a file named exercise.py with this code inside it:
def average(num1, num2):
 (number, number) -> number
Return the average of num1 and num2.
average(10,20)
15.0
average(2.5, 3.0)
2.75
return num1 + num2 / 2
a. Run exercise.py . Import doctest and run doctest.testmod() .
b. Both of the tests in function average ’s docstring fail. Fix the code and
rerun the tests. Repeat this procedure until the tests pass.
"""

import doctest


def average(num1, num2):
    """

    (number, number) -> number

    Return the average of num1 and num2.
    """
    return (num1 + num2) / 2


print(average(10, 20))
print(average(2.5, 3.0))

print(doctest.testmod())
