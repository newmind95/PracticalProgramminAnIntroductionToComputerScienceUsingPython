"""
Using string method find , write a single expression that produces the index
of the second occurrence of o in 'tomato' . Hint: Call find twice.
"""

my_str = 'tomato'
print(my_str.find('o', my_str.count('o') + 1))
