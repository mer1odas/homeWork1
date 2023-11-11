import random
a1 = []

def rand(a):
    rand_chislo = random.randrange(0, a + 1)
    while rand_chislo in a1:
        rand_chislo = random.randrange(0, a + 1)
    a1.append(rand_chislo)
    return rand_chislo
print(rand(1))
print(rand(1))