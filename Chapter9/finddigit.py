s = 'AudiQ5G-Tron'
digit_index = -1    # This will be -1 until we find a digit
for i in range(len(s)):
    # if we found a digit
    if s[i].isdigit():
        digit_index = i
        break

print(digit_index)
