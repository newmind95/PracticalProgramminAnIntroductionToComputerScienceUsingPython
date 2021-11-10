bird_to_observation = {}

bird_to_observation['snow gooes'] = 33
print(bird_to_observation)

bird_to_observation['eagle'] = 999
print(bird_to_observation)

bird_to_observation['eagle'] = 9
print(bird_to_observation)

if 'eagle' in bird_to_observation:
    print('eagles have been seen')

if 'snow gooes' in bird_to_observation:
    print('snow gooes have been seen')
