"""
Variable fruit refers to 'pineapple' . For the following function calls, in what
order are the subexpressions evaluated?
a. fruit.find('p', fruit.count('p'))
b. fruit.count(fruit.upper().swapcase())
c. fruit.replace(fruit.swapcase(), fruit.lower())
"""

fruit = 'pineapple'

print(fruit.find('p', fruit.count('p')))
print(fruit.count(fruit.upper().swapcase()))
print(fruit.replace(fruit.swapcase(), fruit.lower()))
