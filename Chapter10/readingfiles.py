#with open('file_example.txt', 'r') as file:
 #   contents = file.read()
# print(contents)


def sum_number_pairs(input_file, output_filename):
    with open(output_filename, 'w') as output_filename:
        for number_pair in input_file:
            number_pair = number_pair.strip()
            operands = number_pair.split()
            total = float(operands[0]) + float(operands[1])
            new_line = '{0} {1}\n'.format(number_pair, total)
            output_filename.write(new_line)


print(sum_number_pairs('number_pairs.txt', 'number_pairs.txt'))
