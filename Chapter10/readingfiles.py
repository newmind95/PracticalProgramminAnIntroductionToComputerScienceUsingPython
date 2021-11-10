with open('file_example.txt', 'r') as file:
    contents = file.read()

print(contents)

with open('file_example.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()

print('The first 10 characters:', first_ten_chars)
print('The rest of the characters:', the_rest)

print('====================================')
print()

with open('file_example.txt', 'r') as example_file:
    lines = example_file.readlines()

print(lines)

print('====================================')
print()

with open('planets.txt', 'r') as read_file:
    planets = read_file.readlines()
print(planets)

for planet in reversed(planets):
    print(planet.strip())

print('======================================')
print()

for planet in sorted(planets):
    print(planet.strip())

print('=======================================')
print()

with open('scores.txt', 'r') as read_scores:
    scores = read_scores.read()
print(scores)

