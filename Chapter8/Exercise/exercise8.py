def is_longer(L1, L2):
    """
    (list, list) -> bool

    Return True if and only if the length of L1 is
    longer than the length of L2
    """

    if len(L1) > len(L2):
        return True
    else:
        return False


print(is_longer([1, 2, 3], [4, 5]))
print(is_longer([1, 2, 3], [4, 5, 6, 7]))
print(is_longer(['abcdef'], ['ab', 'cd', 'ef']))
print(is_longer(['a', 'b', 'c'], [1, 2, 3]))