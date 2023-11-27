a = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
for i in range(len(a)):
    q = ""
    for i1 in a[i]:
        q = q + str(i1)
    a[i] = int(q)
print(a)