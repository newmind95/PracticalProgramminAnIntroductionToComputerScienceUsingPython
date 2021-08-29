#for num in range(10):
 #   print(num)

total = 0
for i in range(1, 101):
    total = total + i

print(total)

print('===============================')

values = [4, 10, 3, 8, -6]
for num in values:
    num = num * 2
    print(num)

print(values)

print('=============================')

values = [4, 10, 3, 8, -6]
print(len(values))

print(list(range(5)))

print(list(range(len(values))))

for i in range(len(values)):
    print(i)

print('============================')

for i in range(len(values)):
    print(i, values[i])

print('=============================')
for i in range(len(values)):
    values[i] = values[i] * 2

print(values)

print('===============================')

values = [4, 10, -20, -30]
print(values)

print(list(range(len(values))))

for i in range(len(values)):
    print(i, values[i])

for i in range(len(values)):
    values[i] = values[i] * 2

print(values)

print('=================================')

metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]

for i in range(len(metals)):
    print(metals[i], weights[i])

names = ['John', 'Jane', 'Jack', 'Aaron', 'Ben']
scores =[67.2, 32.4, 45.5, 63.2, 52.4]

for i in range(len(names)):
    print('Name:', names[i], ', Score: ', scores[i])

print('===================================')

teams = ['Arsenal', 'Chelsea', 'Manchester United', 'Manchester City']
points = [92, 90, 82, 81]

for i in range(len(teams)):
    print('Team:', teams[i], ', Points:', points[i])
