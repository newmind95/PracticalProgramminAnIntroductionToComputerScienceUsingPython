def complement(L):
    """
    (list of string) -> string

    Return the newly DNA sequence of the complement of a DNA.
    """

    result = ''

    for i in range(len(L)):
        # Find the character As and replace them with Ts
        if L[i] == 'A':
            result += 'T'

        # Find the character Ts and replace them with As
        elif L[i] == 'T':
            result += 'A'

        # Find the character Cs and replace them with Gs
        elif L[i] == 'C':
            result += 'G'

        # Find the character Gs and replace them with Cs
        elif L[i] == 'G':
            result += 'C'

    # Return result
    return result


print(complement('AATTGCCGT'))
