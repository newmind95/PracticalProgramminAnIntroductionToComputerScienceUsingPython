observations_file = open('arcticbirds.txt')
bird_observed = set()
for line in observations_file:
    bird = line.strip()
    bird_observed.add(bird)

print(bird_observed)
