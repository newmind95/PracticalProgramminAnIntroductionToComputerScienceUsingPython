"""
Following the function design recipe, define a function that has one
parameter, a distance in kilometers, and returns the distance in miles.
(There are 1.6 kilometers per mile.)
"""


def get_distance_in_miles(distance_in_kilometers):
    get_kilometers_per_mile = 1.6
    """
    (float) -> float
        
    Returns the distance in miles.
    There are 1.6 kilometers per mile. 
    """
    return distance_in_kilometers / get_kilometers_per_mile


print(get_distance_in_miles(3))
print(get_distance_in_miles(1))
print(get_distance_in_miles(20))
