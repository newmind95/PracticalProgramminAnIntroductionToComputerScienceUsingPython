"""
Using nested for loops, print the triangle described in the previous exercise
with its hypotenuse on the left side:

      T
     TT
    TTT
   TTTT
  TTTTT
 TTTTTT
TTTTTTT
"""


def print_triangle(rows):
    """
    (int) -> str

    Return triangle printed with its hypotenuse on the left side
    """

    spaces = rows - 1

    for i in range(0, rows):
        for j in range(0, spaces):
            print(end=' ')

        spaces = spaces - 1

        for j in range(0, i + 1):
            print('T', end='')
        print()


print_triangle(7)


