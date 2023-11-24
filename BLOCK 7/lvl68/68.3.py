a = []
q = 0
for i in range(1, 6):
    if len(a) != 0: 
        a.append(a[q] + str(i))
        q += 1
    else:
        a.append(str(i))
for i in reversed(range(len(a) - 1)):
    a.append(a[i])
print(a)