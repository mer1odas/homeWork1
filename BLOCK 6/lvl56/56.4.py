import math

def dele(a : list):
    a1 = []
    for i in range(len(a)):
        for i1 in range(1, round(math.sqrt(a[i])) + 1):
            if a[i] % i1 == 0:
                a1.append(i1)
                if a[i] / i1 != i1:
                    a1.append(round(a[i] / i1))
        a[i] = a1
        a1 = []
    return a

print(dele([10]))