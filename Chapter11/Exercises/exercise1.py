def find_dups(list_nums):

    xset = set(list_nums)
    yset = []
    dups = []
    count = 0

    for i in xset:
        yset.append(i)

    for i in yset:
        for j in list_nums:
            if i == j:
                count += 1
            if count >= 2:
                dups.append(i)
                break
        count = 0

    return dups


list_nums = [1, 1, 1, 2, 2, 3, 3, 3]
print(find_dups(list_nums))
