lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lst1 = []
for i in range(0, 10, 3):
    lst1.append(lst[i : i + 3])
print(lst1)