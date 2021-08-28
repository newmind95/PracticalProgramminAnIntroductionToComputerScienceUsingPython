"""
In this exercise, you’ll create a list and then answer questions about that
list.
a. Create a list of temperatures in degrees Celsius with the values 25.2,
16.8, 31.4, 23.9, 28, 22.5, and 19.6, and assign it to a variable called
temps .
b. Using one of the list methods, sort temps in ascending order.
c. Using slicing, create two new lists, cool_temps and warm_temps , which contain
the temperatures below and above 20 degrees Celsius, respectively.
d. Using list arithmetic, recombine cool_temps and warm_temps into a new
list called temps_in_celsius .
"""

# Create a list of temperatures
temps = ['16.8', '31.4', '23.9', '28', '22.5', '19.6']
temps.sort()    # sort temps in ascending order
print(temps)

cool_temps = temps[0:2]     # contains temperature below 20
warm_temps = temps[2:6]     # contains temperature above 20

print(cool_temps)
print(warm_temps)

temps_in_celsius = cool_temps + warm_temps

print(temps_in_celsius)
