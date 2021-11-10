def skip_header(reader):
    """
    (file open for reading) -> str

    Read and return the first real piece of data
    """

    # Read the description line
    line = reader.readline()

    # Find and read the non-comment data
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the real piece of data
    return line


def process_file(reader):
    """
    (file open for reading) -> str
    Read and print the data from reader, which starts with a
    single description line, then a sequence of '#',
    then a sequence of data
    """

    # Find and print the first piece of data
    line = skip_header(reader).strip()
    print(line)

    # Read the rest of the data
    for line in reader:
        line = line.strip()
        print(line)


if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)
