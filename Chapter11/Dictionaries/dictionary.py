observation_file = open('arcticbirds.txt')
bird_to_observations = {}
for line in observation_file:
    bird = line.strip()
    if bird in bird_to_observations:
        bird_to_observations[bird] += 1
    else:
        bird_to_observations[bird] = 1

observation_file.close()

for bird, observations in bird_to_observations.items():
    print(bird, observations)
