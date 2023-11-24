q = ""
for i in range(1, 4):
    q = q + "-" + "x" * i
for i in reversed(range(1, 3)):
    q = q + "-" + "x" * i
print(q)