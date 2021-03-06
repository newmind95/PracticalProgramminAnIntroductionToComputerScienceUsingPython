"""
Variable appointments refers to the list
 ['9:00', '10:30', '14:00', '15:00', '15:30'] . An
appointment is scheduled for 16:30, so '16:30' needs to be added to the
list

a. Using list method append , add '16:30' to the end of the list that appoint-
ments refers to.
b. Instead of using append , use the + operator to add '16:30' to the end of
the list that appointments refers to.
c.
You used two approaches to add '16:30' to the list. Which approach
modified the list and which approach created a new list?
"""


appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
print(appointments)
#print(appointments.append('16:30'))  - modified the list
print(appointments + ['16:30']) # created a new list
