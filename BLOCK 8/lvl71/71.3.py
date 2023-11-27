a = [
	[1, 2, 3],
	[9, 2, 3],
	[0, 1, 1],
	[5, 7, 1],
]
sum1 = 0
sum2 = 0
b = a
for i in range(len(b)):
    for i1 in a[i]:
        sum1 += i1
    if sum1 > sum2:
        a[i], a[i - 1] = a[i - 1], a[i]
    sum2 = sum1
    sum1 = 0
print("end", a[::-1])