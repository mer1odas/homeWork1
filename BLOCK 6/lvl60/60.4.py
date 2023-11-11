import math

def dele(a):
    a1 = []
    a2 = []
    a3 = []
    for i in range(1, round(math.sqrt(a)) + 1):
        if a % i == 0:
            a1.append(i)
            if a / i != i:
                a1.append(round(a / i))
    for i1 in a1:
        for i2 in range(1, round(math.sqrt(i1)) + 1):
            if i1 % i2 == 0:
                a2.append(i2)
                if i1 / i2 != i2:
                    a2.append(round(i1 / i2))
        if len(a2) <= 2:
            a3.append(i1)
        a2 = []
    return a3

print(dele(10))