def dele(a : list):
    b = a.copy()
    for i in range(0, len(a) - 1):
            # print(i)
            if a[i] == a[i + 1]:
               b.remove(a[i])
               b.remove(a[i + 1])
    return b

print(dele([1, 1, 3, 4, 5, 3, 6, 6]))