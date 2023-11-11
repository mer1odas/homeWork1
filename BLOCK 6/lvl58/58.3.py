import random
q = []

def func(a):
    sum1 = 0
    index = random.randrange(0, len(a))
    while index in q:
        sum1 += 1
        index = random.randrange(0, len(a))
    q.append(index)
    if len(q) > 1:
        q.remove(q[0])
    return a[index]

print(func([1, 2, 3]))
print(func([1, 2, 3]))
print(func([1, 2, 3]))
print(func([1, 2, 3]))
print(func([1, 2, 3]))
print(func([1, 2, 3]))
print(func([1, 2, 3]))
print(func([1, 2, 3]))
