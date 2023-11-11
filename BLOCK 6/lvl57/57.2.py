def spis(lst1, lst2):
    for i in lst2:
        lst1.append(i)
    return lst1

print(spis([1, 2, 3], [1, 2, 3]))