a = [
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
	[1, 2, 3, 4, 5],
]
sum1 = 0
q = []
for i in range(len(a)):
    for i1 in range(len(a)):
        sum1 += a[i1][i]
    q.append(sum1)
    sum1 = 0
print(q)