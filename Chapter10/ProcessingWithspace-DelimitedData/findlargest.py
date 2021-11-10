import time_series


def find_largest(line):
    """
    (str) -> int

    Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.
    """

    # The largest value seen so far
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a largest value, remember it.
        if v > largest:
            largest = v

    return largest


def process_file(reader):
    """
    (file open for reading) -> int

    Read and process reader, which must be start with time_series header.
    Return the largest value after the header. There may be multiple pieces
    of data on each line.
    """

    line = time_series.skip_header(reader).strip()
    # The largest value so far is the largest on this first line of data.
    largest = find_largest(line)

    # Check the rest of the lines for larger values
    for line in reader:
        large = find_largest(line)
        if largest < large:
            largest = large

    return largest


if __name__ == '__main__':
    with open('lynxpelts.txt', 'r') as input_files:
        print(process_file((input_files)))
