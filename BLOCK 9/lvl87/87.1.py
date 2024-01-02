a = [
	[11, 12, 13, 14, 15],
	[21, 22, 23, 24, 25],
	[31, 32, 33, 34, 35],
	[41, 42, 43, 44, 45],
	[51, 52, 53, 54, 55],
]
for i in range(len(a)):
    for i1 in range(len(a[i])):
        if i1 != i and i1 != len(a[i]) - 1 - i:
            a[i][i1] = 0
print(a)