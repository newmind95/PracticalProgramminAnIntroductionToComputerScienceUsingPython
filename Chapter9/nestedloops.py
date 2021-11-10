outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']

for metal in outer:
    for halogen in inner:
        print(metal + halogen)


def print_numbers(n):

    numbers = list(range(1, n + 1))

    for i in numbers:
        print('\t' + str(i), end='')

    print()

    for i in numbers:
        print(i, end='')
        for j in numbers:
            print('\t' + str(i * j), end='')

        print()


print(print_numbers(5))
