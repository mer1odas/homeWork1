import random

def func(n):
    a = []
    for i in range(n):
        chislo = random.randrange(1, 11)
        while chislo in a:
            chislo = random.randrange(1, 11)
        a.append(chislo)
    return a

print(func(5))