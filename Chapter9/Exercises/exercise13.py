"""
Using nested for loops, print a right triangle of the character T on the
screen where the triangle is one character wide at its narrowest point and
seven characters wide at its widest point:
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
"""

rows = 7
for i in range(rows + 1):
    for j in range(i):
        print('T', end='')
    print()

