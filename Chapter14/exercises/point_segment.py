import math

"""
Consider this code:
>>> segment = LineSegment(Point(1, 1), Point(3, 2))
>>> segment.slope()
0.5
>>> segment.length()
2.23606797749979

In this exercise, you will write two classes, Point and LineSegment , so that
you can run the code above and get the same results.
a. Write a Point class with an __init__ method that takes two numbers as
parameters.

b. In the same file, write a LineSegment class whose constructor takes two
Point s as parameters. The first Point should be the start of the segment.

c.Write a slope method in the class LineSegment that computes the slope
of the segment. (Hint: The slope of a line is rise over run.)

d. Write a length method in class LineSegment that computes the length of
the segment. (Hint: Use x ** n to raise x to the n th power. To compute
the square root, raise a number to the (1/2) power or use math.sqrt .)
"""

class Point:
    def __init__(self, x, y):
        """ (Point, x, y) -> NoneType

        A new point at position (x, y)

        >>> p = Point(1, 3)
        >>> p.x
        1
        >>> p.y
        3
        """

        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, point1, point2):
        """ (LineSegment, Point, Point) -> NoneType

        >>> p1, p2 = Point(1, 1), Point(3, 2)
        >>> segment = LineSegment(p1, p2)
        """

        self.start_point = point1
        self.end_point = point2


    def slope(self):
        """ (LineSegment) -> float

        Computes the slope of the segment.
        
        >>> segment = LineSegment(Point(1, 1), Point(3, 2))
        >>> segment.slope()
        0.5
        """

        return (self.end_point.y - self.start_point.y) \
               / (self.end_point.x - self.start_point.x)


    def length(self):
        """ (LineSegment) -> float

        Computes the length of the segment

        >>> segment.length()
        2.23606797749979
        """

        return math.sqrt(
            (self.end_point.y - self.start_point.y) ** 2 \
            + (self.end_point.x - self.start_point.x) ** 2)
        

p = Point(1, 3)
print(p.x)
print(p.y)

p1, p2 = Point(1, 1), Point(3, 2)
segment = LineSegment(p1, p2)
print(segment.start_point == p1)
print(segment.end_point == p2)
print(segment.slope())
print(segment.length())
