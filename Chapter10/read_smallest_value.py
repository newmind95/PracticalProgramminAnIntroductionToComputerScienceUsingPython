import time_series


def smallest_value(reader):

    line = time_series.skip_header(reader).strip()

    # Now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        value = int(line.strip())

        # If we find a smaller value, remember it.
        smallest = min(smallest, value)

    return smallest


def smallest_value_skip(reader):
    """
    (file open for reading) -> NoneType
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header. Skip missing values,
    which are indicated with hyphen.
    """

    line = time_series.skip_header(reader).strip()

    smallest = int(line)

    for line in reader:
        value = int(line.strip())

        if value < smallest:
            smallest = value

    return smallest


def largest_value_skip(reader):
    """
    (file open for reading) -> NoneType
    Read and process reader, which must start with a time_series header.
    Return the  value after header. Skip missing values, which
    are indicated with hyphen.
    """

    line = time_series.skip_header(reader)
    # Now lines contains the first data value; this is
    # also the  value found so far.
    largest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            largest = max(largest, value)

    return largest


if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print('Smallest value:', smallest_value_skip(input_file))
        #print('Largest value:', largest_value_skip(input_file))
