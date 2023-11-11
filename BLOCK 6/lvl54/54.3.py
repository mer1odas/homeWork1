import math

def dele(a):
    a1 = []
    for i in range(1, round(math.sqrt(a)) + 1):
        if a % i == 0:
            a1.append(i)
            a1.append(round(a / i))
    return a1

print(dele(4))