import math

def dele(a : list):
    a1 = []
    dele = []
    sum1 = 0
    for i in range(len(a)):
        for i1 in range(1, round(math.sqrt(a[i])) + 1):
            if a[i] % i1 == 0:
                a1.append(i1)
                if a[i] / i1 != i1:
                    a1.append(round(a[i] / i1))
        a[i] = a1
        a1 = []
    for q in range(len(a[0])):
        for q1 in a:
            if a[0][q] in q1:
                sum1 += 1
            if sum1 == len(a):
                dele.append(a[0][q])
        sum1 = 0
    return dele

print(dele([3, 6, 9]))