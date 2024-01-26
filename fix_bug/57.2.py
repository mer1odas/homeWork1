def spis(lst1, lst2):
    lst3 = []
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3

print(spis([1, 2, 3], [1, 2, 3, 4]))