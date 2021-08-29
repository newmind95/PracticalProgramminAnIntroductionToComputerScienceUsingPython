country = 'United States of America'
for ch in country:
    if ch.isupper():
        print(ch)

print('===================================')

for ch in country:
    if ch.islower():
        print(ch)

print('=====================================')

for ch in country:
    if ch.isascii():
        print(ch)
    