"""
Following the function design recipe, define a function that has four
parameters, all of them grades between 0 and 100 inclusive, and returns
the average of the best 3 of those grades. Hint: Call the function that you
defined in the previous exercise.
"""


def func_grades(grade1, grade2, grade3, grade4):
    """
    (int, int, int, int) -> float

    Return the average of the best 3 of those grades

    func_grades(40, 53, 43, 50)
    48.667
    func_grades(50, 32, 22, 60)
    47.333
    """
    min_grade = min(grade1, grade2, grade3, grade4)
    add_all_grades = (grade1 + grade2 + grade3 + grade4)
    best_three = (add_all_grades - min_grade) / 3

    return best_three


print('Average of the best 3 grades: {:.3f}'.format(func_grades(50, 32, 22, 60)))
