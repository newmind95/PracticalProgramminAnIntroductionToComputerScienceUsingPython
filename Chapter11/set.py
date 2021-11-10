score1 = {5, 6, 2, 3, 4}
score2 = {5, 2, 3, 7, 8}

print(score1)
print(score2)

print(score1.difference(score2))
print('Intersection:', score1.intersection(score2))
print(score1.issubset(score2))
print(score1.issuperset(score2))

print(score1 - score2)

print(score1 & score2)

print(score1 <= score2)

print(score1 >= score2)

print(score1 | score2)

print(score1 ^ score2)
