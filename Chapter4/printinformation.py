print('In 1859, Charles Darwin revolutionized biology')
print('and our understanding of ourselves')
print('by publishing "On the Origin of Species"')

radius = 5
print("The diameter of the circle is", radius * 2, "cm.")


print()


def convert_to_celsius(fahrenheit):
    """
    (number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.
    """
    return (fahrenheit - 32.0) * 5 / 9


print('80, 78.8, and 10.4 degrees Fahrenheit are equal to ', end='')
print(convert_to_celsius(80), end=', \n')
print(convert_to_celsius(78.8), end=', and ')
print(convert_to_celsius(10.4), end=' Celsius.\n')
