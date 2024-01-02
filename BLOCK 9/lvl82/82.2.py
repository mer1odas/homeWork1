import math
a = int(input())
a1 = []
for i in range(1, round(math.sqrt(a)) + 1):
    if a % i == 0:
        a1.append(i)
        if a / i != i:
            a1.append(round(a / i))
a1.sort()
mnojit = []
for i in range(len(a1)):
    mnojit.append([a1[i], a1[len(a1) - (1 + i)]])
print(mnojit)