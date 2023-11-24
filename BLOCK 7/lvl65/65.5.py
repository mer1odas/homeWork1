a = []
a1 = ["x", "x", "x", "x", "x"]
for i in range(1, 6):
    a.append(a1.copy())
    a1.remove("x")
print(a)