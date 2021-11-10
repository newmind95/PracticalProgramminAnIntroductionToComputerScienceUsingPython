"""
In The Readline Technique, on page 179, you learned how to read some
files from the Time Series Data Library. In particular, you learned about
the Hopedale data set, which describes the number of colored fox fur pelts
produced from 1834 to 1842. This file contains one value per year per
line.

a. Write an outline in English of the algorithm you would use to read
the values from this data set to compute the average number of pelts
produced per year.

b. Translate your algorithm into Python by writing a function named
hopedale_average that takes a filename as a parameter and returns the
average number of pelts produced per year.

"""

def skip_header(reader):
    """
    (file open for reading) -> str

    Skip the header in reader and return the first real piece of data.
    """

    # Read the non-comment line
    line = reader.readline()

    # Find the first real piece of data
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains real piece of data
    return line


def hopedale_average(reader):
    """
    (file open for reading) -> str

    Read and process the average of pelts produced per year.
    """

    line = skip_header(reader).strip()

    average = float(line)

    for line in reader:
        value = float(line.strip())

        average = average + value / 2

    return average


if __name__ == '__main__':
    with open('hope_dale.txt', 'r') as input_file:
        print(hopedale_average(input_file))
