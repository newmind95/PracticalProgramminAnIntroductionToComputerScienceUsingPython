def skip_header(reader):
    """
    (file to open for reading) -> str

    Skip the header in reader and returns the real piece of data
    """

    # Read the description line
    line = reader.readline()

    # Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the real data
    return line


def process_file(reader):

    line = skip_header(reader).strip()
    print(line)

    for line in reader:
        line = line.strip()
        print(line)


if __name__ == '__main__':
    with open('lynxpelts.txt', 'r') as input_file:
        process_file(input_file)
