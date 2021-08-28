"""
1. Variable kingdoms refers to the list
['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi',
'Animalia'] .
Using kingdoms and either slicing or indexing with positive indices,
write expressions that produce the following:
a. The first item of kingdoms
b. The last item of kingdoms
c. The list ['Bacteria', 'Protozoa', 'Chromista']
d. The list ['Chromista', 'Plantae', 'Fungi']
e. The list ['Fungi', 'Animalia']
f. The empty list
"""

kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
print('First item in the list: {0}'.format(kingdoms[0]))
print('Last item in the list: {0}'.format(kingdoms[-1]))
print('List: {0}'.format(kingdoms[:3]))
print('List: {0}'.format(kingdoms[2:-1]))
print('List: {0}'.format(kingdoms[4:]))
print('List: ', kingdoms.clear())
