import random

def func(a):
    idex = random.randrange(0, len(a))
    return a[idex]

print(func([1, 2, 3]))
