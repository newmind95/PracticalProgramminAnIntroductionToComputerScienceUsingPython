age = 25
bmi = 22
young = age < 45
slim = bmi < 22.0
if age < 45:
    if bmi < 22.0:
        risk = 'low'
    else:
        if bmi < 22.0:
            risk = 'medium'
        else:
            risk = 'high'
print(risk)
