import country

"""
a. Here is a sample interaction from the Python shell:
>>> canada = country.Country('Canada', 34482779, 9984670)
>>> usa = country.Country('United States of America', 313914040, 9826675)
>>> mexico = country.Country('Mexico', 112336538, 1943950)
>>> countries = [canada, usa, mexico]
>>> north_america = Continent('North America', countries)
>>> north_america.name
'North America'
>>> for country in north_america.countries:
print(country)
Canada has a population of 34482779 and is 9984670 square km.
United States of America has a population of 313914040 and is 9826675 
square km.
Mexico has a population of 112336538 and is 1943950 square km.

The code above cannot be executed yet, because class Continent does
not exist. Define Continent with a constructor (method __init__ ) that has
three parameters: a continent, its name, and its list of Country objects.
b. Consider this code:
>>> north_america.total_population()
460733357
In class Continent , define a method named total_population that returns
the sum of the populations of the countries on this continent.
"""

class Continent:
    """A continent named name, and list of Country objects."""


    def __init__(self, name, countries):
        """(Continent, str, list) -> NoneType
        Create a continent named name, and list of countries.
        """
        self.name = name
        self.countries = countries


    def __str__(self):
        res = self.name
        for country in self.countries:
            res += '\n' + str(country)

        return res


    def total_population(self):
        """ (Continent) -> int"""
        total = 0
        for country in self.countries:
            total += country.population
        return total
    
canada = country.Country('Canada', 34482779, 9984670)
usa = country.Country('United States of America', 313914040, 9826675)
mexico = country.Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)    
print(north_america.total_population())
print(north_america)
