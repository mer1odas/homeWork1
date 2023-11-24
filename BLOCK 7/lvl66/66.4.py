sum1 = 0
sum2 = 0
q =[]
for i in range(1001, 1000000):
    i_str = str(i)
    while len(i_str) < 6:
        i_str = "0" + i_str
    for i1 in i_str[0 : 3]:
        sum1 += int(i1)
    for i2 in i_str[3 : 6]:
        sum2 += int(i2)
    if sum1 == sum2:
        q.append(i_str)
    sum1 = 0
    sum2 = 0
file = open("txt.txt", "w")
for i in q:
    file.write(i + "\n")