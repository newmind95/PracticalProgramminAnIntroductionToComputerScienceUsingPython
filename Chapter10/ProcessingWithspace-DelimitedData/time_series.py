def skip_header(reader):
    """
    (file open for reading) -> str
    Skip the header in reader and return the first piece of data.
    """

    # Read the description line
    line = reader.readline()

    # Find the first non-comment line
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the real piece of data
    return line


def process_file(reader):

    line = skip_header(reader).strip()
    print(line)

    # Read the rest of the data
    for line in reader:
        line = line.strip()
        print(line)