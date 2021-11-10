"""
Edsgar Dijkstra is known for his work on programming languages. He
came up with a neat problem that he called the Dutch National Flag
problem: given a list of strings, each of which is either 'red' , 'green' , or 'blue'
(each is repeated several times in the list), rearrange the list so that the
strings are in the order of the Dutch national flag—all the 'red' strings
first, then all the 'green' strings, then all the 'blue' strings.

Write a function called dutch_flag that takes a list and solves this problem.
"""


def dutch_flag(seq, order=('red', 'green', 'blue')):

    """

    (list of strings) -> list of strings

    Rearrange the list so that the strings are in the order
    of the Dutch national flag.

    ['red', 'blue', 'green', 'blue', 'red', 'green', 'red', 'blue', 'green']

    ['red', 'red', 'red', 'green', 'green', 'green', 'blue', 'blue', 'blue']
    """

    return sorted(seq, key=order.index)


L = ['red', 'blue', 'green', 'blue', 'red', 'green', 'red', 'blue', 'green']
print(dutch_flag(L))
