def remove_duplicates(t):
    ls = []
    for x in t:
        if ls.count(x) > 0:
            pass
        else:
            ls.append(x)
    return ls