"""In this exercise, you will implement class Country , which represents a
country with a name, a population, and an area.

a. Here is a sample interaction from the Python shell:
>>> canada = Country('Canada', 34482779, 9984670)
>>> canada.name
'Canada'
>>> canada.population
34482779
>>> canada.area
9984670
"""

"""b. Consider this code:
>>> canada = Country('Canada', 34482779, 9984670)
>>> usa = Country('United States of America', 313914040, 9826675)
>>> canada.is_larger(usa)
True
In class Country , define a method named is_larger that takes two Country
objects and returns True if and only if the first has a larger area than the
second."""

"""c. Consider this code:
>>> canada.population_density()
3.4535722262227995
In class Country , define a method named population_density that returns
the population density of the country (people per square km).
"""

"""d. Consider this code:
>>> usa = Country('United States of America', 313914040, 9826675)
>>> print(usa)
United States of America has a population of 313914040 and is 9826675
square km.

In class Country , define a method named __str__ that returns a string
representation of the country in the format shown above."""

class Country:
    """Country that has name, population, and its area."""


    def __init__(self, name, population, area):
        """(Country, str, int, int) -> NoneType

        Create a contry named name, with population, and its area.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.name
        'Canada'
        >>> canada.population
        34482779
        >>> canada.area
        9984670
        """

        self.name = name
        self.population = population
        self.area = area


    def __str__(self):
        """(Country) -> str
        Return a string representation of the country in the
        format shown below.

        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> print(usa)
        United States of America has a population of 313914040 and is 9826675
        square km.
        """
        return f'{self.name} has a population of {self.population} ' \
               f'and is {self.area} square km.'


    def __repr__(self):
        """(Country) -> str
        Return a string representation that behaves like this:

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada
        Country('Canada', 34482779, 9984670)
        >>> [canada]
        [Country('Canada', 34482779, 9984670)]
        """
        return f'Country({self.name}, {self.population}, {self.area})'
    

    def is_larger(self, other):
        """(Country, Country) -> bool
        Return True iff the first has a larger area than the second.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> canada.is_larger(usa)
        True
        """
        return self.area > other.area


    def population_density(self):
        """(Country) -> float

        Return the population density of the country
        (people per square km)

        >>> canada.population_density()
        3.4535722262227995
        """
        density = self.population / self.area
        return density


##canada = Country('Canada', 34482779, 9984670)
##print(canada.name)
##print(canada.population)
##print(canada.area)
##print(canada.population_density())
##print(canada)
##print([canada])

##usa = Country('United States of America', 313914040, 9826675)
##print(canada.is_larger(usa))
##print(usa)
