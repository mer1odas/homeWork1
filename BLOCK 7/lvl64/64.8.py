a = []
a1 = [1]
for i in range(2, 8):
    a2 = a1.copy()
    a.append(a2)
    a1.append(i)
print(a)