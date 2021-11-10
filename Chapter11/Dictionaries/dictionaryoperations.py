scientist_to_birthday = {'Newton' : 1642, 'Darwin' : 1809,
                         'Turing' : 1912}

print(scientist_to_birthday.keys())
print(scientist_to_birthday.values())

print(scientist_to_birthday.items())
print(scientist_to_birthday.get('Newton'))

print(scientist_to_birthday.setdefault('Newton'))
print(scientist_to_birthday.setdefault('Darwin'))
