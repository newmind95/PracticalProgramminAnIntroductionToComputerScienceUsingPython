def mating_pairs(males, females):
    x_set = {males, females}
    x_tuple = tuple(x_set)

    return x_tuple


male = ''
female = ''
count = 0

if male == female:
    male = input('Enter male name:')
    female = input('Enter female name: ')
    print(mating_pairs(male, female))
