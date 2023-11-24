a = []
a1 = []
for i in range(1, 6):
    a1.append("x")
    a.append(a1.copy())
print(a)