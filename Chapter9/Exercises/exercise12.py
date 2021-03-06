"""
Consider this code:
def remove_neg(num_list):
 (list of number) -> NoneType
Remove the negative numbers from the list num_list.

numbers = [-5, 1, -3, 2]
remove_neg(numbers)
numbers
[1, 2]

    for item in num_list:
        if item < 0:
            num_list.remove(item)

When remove_neg([1, 2, 3, -3, 6, -1, -3, 1]) is executed, it produces [1, 2, 3, 6, -3, 1] .
The for loop traverses the elements of the list, and when a negative value
(like -3 at position 3) is reached, it is removed, shifting the subsequent
values one position earlier in the list (so 6 moves into position 3). The
loop then continues on to process the next item, skipping over the value
that moved into the removed item’s position. If there are two negative
numbers in a row (like -1 and -3), then the second one won’t be removed.

Rewrite the code to avoid this problem.
"""


def remove_neg(num_list):
    r = num_list[:]
    for item in num_list:
        if item < 0:
            r.remove(item)
    print(r)



numbers = [1, 2, 3, -3, 6, -1, -3, 1]
print(numbers)
remove_neg(numbers)