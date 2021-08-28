def convert_to_celsius(fahrenheit):
    """
    (number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    """
    return (fahrenheit - 32.0) * 5.0 / 9.0


def above_freezing(celsius):
    """
    (float) -> bool

    Return temperature iff temperature celsius degrees in above freezing.
    """
    return celsius > 0


if __name__ == "__main__":
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print("It is above freezing")
    else:
        print("It is below freezing")
