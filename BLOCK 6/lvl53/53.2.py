def dele(a : list):
    for i in a:
        if a.count(i) >= 3:
            for i1 in range(a.count(i)):
                a.remove(i)
    return a

print(dele([1, 1, 2, 2, 2]))