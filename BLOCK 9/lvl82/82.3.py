import math
a1 = int(input())
a2 = int(input())
q = []
prost = set()
for i1 in range(min(a1, a2), max(a1 ,a2)):
    for i in range(1, round(math.sqrt(i1)) + 1):
        if i1 % i == 0:
            q.append(i)
            if i1 / i != i:
                q.append(round(i1 / i))
    if len(q) <= 2:
        prost.add(i1)
    q = []
print(prost)
    