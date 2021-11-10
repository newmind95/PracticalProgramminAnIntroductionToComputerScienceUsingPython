"""
Variables rat_1_weight and rat_2_weight contain the weights of two rats at the
beginning of an experiment. Variables rat_1_rate and rat_2_rate are the rate
that the rats’ weights are expected to increase each week (for example, 4
percent per week).

a. Using a while loop, calculate how many weeks it would take for the
weight of the first rat to become 25 percent heavier than it was
originally.

b. Assume that the two rats have the same initial weight, but rat 1 is
expected to gain weight at a faster rate than rat 2. Using a while loop,
calculate how many weeks it would take for rat 1 to be 10 percent
heavier than rat 2.
"""

rat_1_weight = 4
rat_2_weight = 4

rat_1_rate = 0.04
weeks = 0

current_rat_1 = rat_1_weight
current_rat_2 = rat_2_weight

while current_rat_1 > rat_1_weight * 0.25:
    rat_1_weight = rat_1_weight + rat_1_rate * rat_1_weight
    weeks = weeks + 1


print('It would take {0} weeks for rat 1 to become 25 percent'.format(weeks), end='\n'
      'heavier than it was originally\n'
      'And the first rat weight will be: {:.2f}\n'.format(rat_1_weight))

print()

weeks_ten_percent = 0

while current_rat_2 > current_rat_1 * 0.10:
    current_rat_1 = current_rat_1 + rat_1_rate * current_rat_1
    weeks_ten_percent += 1

print('It would take {0} weeks for rat 1 to become 10 percent'.format(weeks_ten_percent), end='\n'
      'heavier than it was originally\n'
      'And the first rat weight will be: {:.2f}'.format(current_rat_1))
