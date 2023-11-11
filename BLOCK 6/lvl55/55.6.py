def dele(n):
    a1 = 1
    a2 = 1
    sum1 = 0
    for i in range(n):
        a1 = a1 + a2
        a2 = a1 + a2
        sum1 += a1 + a2
    return sum1 

print(dele(5))