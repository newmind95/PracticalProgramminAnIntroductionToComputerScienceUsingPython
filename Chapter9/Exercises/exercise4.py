"""
In this exercise, you’ll create a nested list and then write code that per-
forms operations on that list.

a. Create a nested list where each element of the outer list contains the
atomic number and atomic weight for an alkaline earth metal. The
values are beryllium (4 and 9.012), magnesium (12 and 24.305), cal-
cium (20 and 40.078), strontium (38 and 87.62), barium (56 and
137.327), and radium (88 and 226). Assign the list to variable
alkaline_earth_metals .

b. Write a for loop to print all the values in alkaline_earth_metals , with the
atomic number and atomic weight for each alkaline earth metal on a
different line.

c.
Write a for loop to create a new list called number_and_weight that contains
the elements of alkaline_earth_metals in the same order but not nested
"""

alkaline_earth_metals = [['beryllium', 4, 9.012],
                         ['magnesium', 12, 24.305],
                         ['calcium', 20, 40.078],
                         ['strontium', 38, 87.62],
                         ['barium', 56, 137.327],
                         ['radium', 88, 226]]

for items in alkaline_earth_metals:
    print('Earth metals: {0}, Atomic number: {1}, Atomic weight: {2}'.format(items[0],
                                                                             items[1],
                                                                             items[2]))

for number_and_weight in alkaline_earth_metals:
    print(list(number_and_weight))
