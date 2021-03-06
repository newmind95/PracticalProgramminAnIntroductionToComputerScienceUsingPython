"""
Suppose the file alkaline_metals.txt contains the name, atomic number, and
atomic weight of the alkaline earth metals:
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

Write a for loop to read the contents of alkaline_metals.txt and store it in a list
of lists, with each inner list containing the name, atomic number, and
atomic weight for an element. (Hint: Use string.split .)
"""


def read_alkaline_metals(reader):
    """
    (file to open) -> NoneType

    Read the contents of alkaline_metals.txt and store
    it in a list of lists, with each inner list.
    """
    for line in reader:
        line = line.split()
        print(line)


if __name__ == "__main__":
    with open("alkaline_metals.txt", "r") as input_file:
        read_alkaline_metals(input_file)
