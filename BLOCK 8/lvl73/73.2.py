lst = [1, 2, 3, 4, 5, 6]
a = 3
for i in range(a ** 2 - len(lst)):
    lst.append("")
print(lst)