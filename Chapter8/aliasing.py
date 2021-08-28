celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_alias = celegans_phenotypes
celegans_phenotypes[5] = 'Lvl'
print(celegans_phenotypes)
print(celegans_alias)


def remove_last_item(L):
    """
    (list) -> list

    Return list L with the last item removed.

    Precondition: len(L) >= 0
    """
    del L[-1]
    return L


celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
print(remove_last_item(celegans_markers))
print(celegans_markers)