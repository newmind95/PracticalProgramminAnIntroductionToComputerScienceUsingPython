"""
Using string methods, write expressions that produce the following:
a. A copy of 'boolean' capitalized
b. The first occurrence of '2' in 'C02 H20'
c. The second occurrence of '2' in 'C02 H20'
d. True if and only if 'Boolean' begins lowercase
e. A copy of "MoNDaY" converted to lowercase and then capitalized
f. A copy of " Monday" with the leading whitespace removed

"""

print('boolean'.capitalize())
print('CO2 H2O'.find('2'))
print('CO2 H2O'.find('2','CO2 H2O'.find('2') + 1))

print('Boolean'.lower().islower())


