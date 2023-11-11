import math

def dele(a):
    sum1 = 0
    for i in range(1, round(math.sqrt(a)) + 1):
        if a % i == 0:
            sum1 += 1
            if a / i != i:
                sum1 += 1
    return sum1

print(dele(10))

# TYT