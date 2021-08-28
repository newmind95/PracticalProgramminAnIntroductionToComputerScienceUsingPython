"""
Following the function design recipe, define a function that has three
parameters, grades between 0 and 100 inclusive, and returns the average
of those grades.
"""


def get_average_grades(grade1, grade2, grade3):
    """
    (int, int, int) -> float

    :param grade1: first grade
    :param grade2: second grade
    :param grade3: third grade
    :return: the average of those  grades
    """
    return grade1 / grade2 / grade3


print(get_average_grades(30, 40, 50))
print(get_average_grades(20, 10, 70))
