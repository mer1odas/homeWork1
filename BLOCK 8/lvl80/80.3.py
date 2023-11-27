a = [
	[1, 2, 3, 4, 5],
	[1, 2, 3],
	[1, 2],
]
a.sort(reverse=True)
print(a)
max_a = len(a[0])
for i in range(1, len(a)):
    for i1 in range(max_a - len(a[i])):
        a[i].append("")
print(a)