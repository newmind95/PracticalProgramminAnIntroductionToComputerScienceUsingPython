def different(a, b):
    """
    (value, value) -> Boolean value

    Return True if a and b refer to different values
    and should return false otherwise.
    """

    if a != b:
        return True
    else:
        return False


print(different(5, 10))
