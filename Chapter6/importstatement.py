#import math


from math import sqrt, pi
import convertcelsius


print(sqrt(3))

print(pi)
radius = 5
print('area is', pi * radius ** 2)

print('circumference is', 2 * pi * radius)


celsius = convertcelsius.convert_to_celsius(33.3)
print(celsius)
print(convertcelsius.above_freezing(celsius))
