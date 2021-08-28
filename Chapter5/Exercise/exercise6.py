# Function that convert temperature t
# from source units to target units.

def convert_temperatures(t, source, target):
    """
    (float, str, str) -> float

    Return result of the entered degree from source to target.
    """
    if target == "Fahrenheit":
       t += (t * 9 / 5) + 32
       print("Convert from ", source, " to ", target)
    elif target == "Kelvin":
        t += (t + 273.15)
        print("Convert from", source, " to ", target)
    elif target == "Rankine":
        t += (t + 273.15) * 5 / 9
        print("Convert from ", source, " to ", target)
    elif target == "Delisle":
        t += (100 - t) * 3 / 2
        print("Convert from ", source, " to ", target)
    return t


source = "Celsius"
t = float(input('Enter degree in Celsius: '))
target = "Delisle"
print(convert_temperatures(t, source, target))
