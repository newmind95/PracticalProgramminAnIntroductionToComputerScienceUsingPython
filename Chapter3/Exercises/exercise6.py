"""
Following the function design recipe, define a function that has three
parameters, grades between 0 and 100 inclusive, and returns the average
of those grades.
"""


def func_grades(grade1, grade2, grade3):
    """
    (int, int, int) -> float

    Return the average of those grades.

    print(func_grades(30, 20, 10)
    20.000

    print(func_grades(43, 32, 12)
    29.000
    """
    return (grade1 + grade2 + grade3) / 3


grade1 = input('Enter first grade: ')
grade2 = input('Enter second grade: ')
grade3 = input('Enter third grade: ')
print('Average {:.3f}'.format(func_grades(float(grade1), float(grade2), float(grade3))))
