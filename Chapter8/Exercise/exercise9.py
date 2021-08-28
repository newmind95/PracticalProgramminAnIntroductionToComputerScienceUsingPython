"""
Variable units refers to the nested list [['km', 'miles', 'league'],
                                         ['kg', 'pound', 'stone']] .
Using units and either slicing or indexing with positive indices, write
expressions that produce the following:

a. The first item of units (the first inner list)
b. The last item of units (the last inner list)
c. The string 'km'
d. The string 'kg'
e. The list ['miles', 'league']
f. The list ['kg', 'pound']

"""

units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print('The first item of units {0}'.format(units[0]))
print('The last item of units {0}'.format(units[1]))
print('The string {0}'.format(units[0][0]))
print('The string {0}'.format(units[1][0]))
print('The list: {0}'.format(units[0][1:]))
print('The list: {0}'.format(units[1][:2]))

