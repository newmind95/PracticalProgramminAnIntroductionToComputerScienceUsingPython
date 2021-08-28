"""ph = float(input('Enter the pH level: '))
if ph < 7.0:
    print(ph, ' is acidic.')
elif ph > 7.0:
    print(ph, 'is basic.')
"""

"""compound = input('Enter the compound: ')
if compound == "H2O":
    print("Water")
elif compound == "NH3":
    print("Ammonia")
elif compound == "CH4":
    print("Methane")
"""

value = input('Enter the pH level: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, " is acidic.")
    elif ph > 7.0:
        print(ph, " is basic.")
    else:
        print(ph, " is neutral.")
else:
    print("No pH value was given!")
