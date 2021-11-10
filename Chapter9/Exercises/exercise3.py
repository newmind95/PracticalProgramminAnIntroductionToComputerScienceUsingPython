"""
Write a for loop to add 1 to all the values from whales from Section 8.1,
Storing and Accessing Data in Lists, on page 129, and store the converted
values in a new list called more_whales . The whales list shouldn’t be modified.
whales refers to [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3] .
"""

whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]

# old list
print(whales)

for more_whales in whales:
    more_whales = more_whales + 1
    print(more_whales)
