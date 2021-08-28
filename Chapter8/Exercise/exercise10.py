"""
Variable units refers to the nested list [['km', 'miles', 'league'],
                                         ['kg', 'pound', 'stone']] .
Using units and either slicing or indexing with negative indices, write
expressions that produce the following:

a. The first item of units (the first inner list)
b. The last item of units (the last inner list)
c. The string 'km'
d. The string 'kg'
e. The list ['miles', 'league']
f. The list ['kg', 'pound']

"""

units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print('The first item of units: {0}'.format(units[-2]))
print('The last item of units: {0}'.format(units[-1]))
print('The string {0}'.format(units[-2][-3]))
print('The string {0}'.format(units[-1][-3]))
print('The list {0}'.format(units[-2][-2:]))
print('The list {0}'.format(units[-1][:-1]))
