def mystery_function(values):
    """
    (str) -> str

    Return nested list, separated by comma based on the value that is entered.

    mystery_function('Banana')
    [['B'], ['a'], ['n'], ['a'], ['n'], ['a']]

    mystery_function('Apple')
    [['A'], ['p'], ['p'], ['l'], ['e']]

    mystery_function('Audi')
    [['A'], ['u'], ['d'], ['i']
    """
    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)

    return result


print(mystery_function('Banana'))
print(mystery_function('Apple'))
print(mystery_function('Audi'))
