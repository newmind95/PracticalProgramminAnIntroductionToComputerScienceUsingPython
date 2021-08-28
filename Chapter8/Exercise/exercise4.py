"""
Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900] . Using list
methods, do the following:
a. Remove 3382 from the list.
b. Get the index of 9362 .
c. Insert 4499 in the list after 9362 .
d. Extend the list by adding [5566, 1830] to it.
e. Reverse the list.
f. Sort the list.

"""

ids = [2353, 2314, 2956, 3382, 9362, 3900]
print(ids.remove(3382))     # remove 3382 from the list
print(ids)
print(ids.index(9362))      # get the index of 9362
print(ids.insert(4, 4499))  # insert 4499 in the list after 9362
print(ids)
print(ids.append(5566), ids.append(1830))
print(ids)
print(ids.reverse())        # reverse the list
print(ids)
ids.sort()  # sort the list
print('Sort the list: ', ids)
