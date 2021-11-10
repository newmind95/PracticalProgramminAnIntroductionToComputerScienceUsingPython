"""
Redo the previous two exercises using while loops instead of for loops.
"""

rows = 7
i = 1
while i <= rows:
    j = 1
    while j <= i:
        j += 1
        print('T', end='')
    print()
    i += 1


spaces = rows - 1
while i <= rows:
    j = 1
    while j <= rows:
        if j <= rows - i:
            print('', end=' ')
        else:
            print('T', end='')
        j += 1
    i += 1
    print()
