"""
Using a loop, sum the numbers in the range 2 to 22 (inclusive), and then
calculate the average.
"""

sum = 0       # To hold the sum of numbers
average = 0
for i in list(range(2, 22 + 1)):
    sum = sum + i
    average = sum / i

print(sum)
print(average)
