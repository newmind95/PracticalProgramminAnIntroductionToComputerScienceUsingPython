def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third


print(quadratic(2, 3, 4, 0.5))

print(quadratic(2, 3, 4, 1.5))
