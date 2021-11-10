import time_series


def smallest_value(reader):
    """
    (file to open for reading) -> int

    Skip the header in reader and returns the smallest value
    """

    line = time_series.skip_header(reader).strip()

    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)

        # If we find a smaller value, remember it
        smallest = min(smallest, value)

    return smallest


if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value(input_file))
