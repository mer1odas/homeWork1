a = []
a1 = []
for i in range(3):
    a.append([])
    for i1 in range(3):
        for i2 in range(1, 4):
            a1.append(i2)
        a[i].append(a1)
        a1 = []
print(a)