import random

def rand(n, a1, a2):
    q = []
    for i in range(n):
        q.append(random.randrange(a1, a2))
    return q

print(rand(10, 10, 100))