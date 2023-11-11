def dele(a : list):
    for i in range(len(a) - 2):
        a.remove(min(a))
    return min(a)

print(dele([1, 2, 3, 4, 5]))

