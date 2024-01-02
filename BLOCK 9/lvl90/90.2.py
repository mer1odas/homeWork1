a = [
	[11, 32, 13, 44, 55],
	[31, 42, 53, 66, 75],
	[12, 26, 33, 45, 52],
	[15, 22, 35, 64, 57],
	[21, 52, 32, 44, 38],
]
max1 = a[1][0]
min1 = a[1][0]
index1 = ""
index2 = ""
for i in range(len(a)):
    if max1 < max(a[i]):
        max1 = max(a[i])
        index1 = str(i) + str(a[i].index(max(a[i])))
    if min1 > min(a[i]):
        min1 = min(a[i])
        index2 = str(i) + str(a[i].index(min(a[i])))
a[int(index1[0])][int(index1[1])], a[int(index2[0])][int(index2[1])] = a[int(index2[0])][int(index2[1])], a[int(index1[0])][int(index1[1])]
print(a)