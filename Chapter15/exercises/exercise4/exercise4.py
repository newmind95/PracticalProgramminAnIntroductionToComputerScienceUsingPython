"""The following function is broken.
def find_min_max(values):
     (list) -> NoneType

    Print the minimum and maximum value from values.
    

    min_value = None
    max_value = None
    for value in values:

        if value > max_value:
            max_value = value

        if value < min_value:
            min_value = max_value

    print(f'The minimum value is {min_value}')
    print(f'The maximum value is {max_value}')
    
What does it actually do? What line(s) do you need to change to fix it?
"""


def find_min_max(values):
    """ (list) -> NoneType

    Print the minimum and maximum value from values.
    """

    min_value = None
    max_value = None
    for value in values:

        if value > max_value or max_value is None:
            max_value = value

        if value < min_value or min_value is None:
            min_value = value

    print(f'The minimum value is {min_value}')
    print(f'The maximum value is {max_value}')
