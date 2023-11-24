a = int(input())
sum = 0
sum1 = 0
a1 = str(a)
pol1 = str(a)[0 : int(len(a1) / 2)]
pol2 = a1[int(len(a1) / 2) : len(a1)]
for i in pol1:
    sum += int(i)
for i1 in pol2:
    sum1 += int(i1)
if sum == sum1:
    print("счастливй билет")
else:
    print("нет")