import math

def dele(a, q):
    a1 = []
    a2 = []
    for i in range(a, q + 1):
        for i1 in range(1, round(math.sqrt(i)) + 1):
            if i % i1 == 0:
               a1.append(i1)
               if i / i1 != i1:
                   a1.append(round(i / i1))
        if len(a1) <= 2:
            a2.append(i)
        a1 = []
    return a2

print(dele(1, 103121))
