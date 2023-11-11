import math

def deletili(a):
    sum1 = 0
    for i in range(1, round(math.sqrt(a)) + 1):
       if a % i == 0:
        sum1 += i
        if a / i != i:
            sum1 += (round(a / i))
    return sum1

print(deletili(4))