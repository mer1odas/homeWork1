a = [
	[11, 12, 13],
	[21, 22, 23],
	[31, 32, 33],
]
a1 = [
	14, 24, 34
]
for i in range(len(a)):
    a[i].append(a1[i])
print(a)