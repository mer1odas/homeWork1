import math

def dele(a):
    a1 = []
    for i in range(1, round(math.sqrt(a)) + 1):
        if a % i == 0:
            a1.append(i)
            if a / i != i:
                a1.append(a / i)
    if len(a1) > 2:
        return "не простое"
    else:
        return "простое"
    
print(dele(7))