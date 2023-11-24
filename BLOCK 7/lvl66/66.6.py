lst = {
	2018: {
		11: {
			29: [1, 2, 3],
			30: [4, 5],
        },
		12: {
			30: [6, 7],
			31: [8, 9],
    },
    },
	2019: {
		12: {
			29: [10, 11],
			30: [12, 13],
			31: [14, 15],
        }
    },
}
q =[]
for i in lst:
    for i1 in lst[i]:
        for i2 in lst[i][i1]:
            for i3 in lst[i][i1][i2]:
                q.append(i3)
print(q)
