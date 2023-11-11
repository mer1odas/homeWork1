import random

def func(a, n):
    q = []
    for i in range(n):
        idex = random.randrange(0, len(a))
        q.append(a[idex])
    return q

print(func([1, 2, 3], 2))
