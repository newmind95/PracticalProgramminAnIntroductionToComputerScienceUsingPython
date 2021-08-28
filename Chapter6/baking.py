import convertcelsius
import doctest

def get_preheating_instructions(fahrenheit):
    """
    (number) -> string

    Return instructions for preheating the oven in fahrenheit degrees
    and Celsius degrees.

    """
    if __name__ == "__main__":
        cels = str(convertcelsius.convert_to_celsius(fahrenheit))
        fahr = str(fahrenheit)
        return "Preheat oven to " + fahr + " degrees F (" + cels + " degrees C)."
    else:
        "Wrong type"


fahr = float(input("Enter the baking temperature in degrees Fahrenheit: "))
print(get_preheating_instructions(fahr))

print(doctest.testmod())
