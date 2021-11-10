def skip_header(reader):
    """
    (file to open for reading) -> str

    Skip the header in reader and returns the real piece of data
    """

    # Read the description line
    line = reader.readline()

    # Find the first piece of data
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