import random

def func(n, a, a1):
    list = []
    list.append(random.randrange(a, a1 + 1))
    for i in range(n - 1):
            random_chislo = random.randrange(a, a1 + 1)
            while random_chislo in list:
                random_chislo = random.randrange(a, a1 + 1)
            list.append(random_chislo)
    return list
        
print(func(5, 1, 10))

