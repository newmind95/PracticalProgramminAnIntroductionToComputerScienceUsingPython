speed = 2
velocities = [0.0, 9.81, 19.62, 29.43]
#rint('Metric:', velocities[0], 'm/sec;',
 #     'Imperial: ', velocities[0] * 3.28, 'ft/sec')
#print('Metric:', velocities[1], 'm/sec;',
 #     'Imperial: ', velocities[1] * 3.28, 'ft/sec')
#print('Metric:', velocities[2], 'm/sec;',
#      'Imperial: ', velocities[2] * 3.28, 'ft/sec')
#print('Metric:', velocities[3], 'm/sec;',
#     'Imperial: ', velocities[3] * 3.28, 'ft/sec')

for speed in velocities:
    print('Metric:', speed, 'm/sec')

print('Final speed:', speed)