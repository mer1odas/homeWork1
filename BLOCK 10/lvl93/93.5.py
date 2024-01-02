import random
a = [
	[11, 12, 13],
	[21, 22, 23],
	[31, 32, 33],
]
for i in range(len(a)):
    a[i].append(random.randrange(1, 99))
a.append([])
for i in range(4):
    a[3].append(random.randrange(1, 99))
print(a)
