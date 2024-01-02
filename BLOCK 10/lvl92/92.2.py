import math
a = int(input())
a1 = []
for i in range(1, round(math.sqrt(a)) + 1):
    if a % i == 0:
        a1.append(i)
        if a / i != i:
            a1.append(round(a / i))
a1.sort()
a1.remove(a1[len(a1) - 1])
sum1 = 0
for i in a1:
    sum1 += i
if sum1 > a:
    print("избыточное")