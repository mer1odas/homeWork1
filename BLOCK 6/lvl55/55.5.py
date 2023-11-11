import random

def dele(a):
    q = []
    for i in range(a):
        q.append(chr(random.randrange(97, 122)))
    return q

print(dele(12))