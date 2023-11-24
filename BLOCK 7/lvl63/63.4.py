import random
n = int(input())
a = []
for i in range(n):
    a.append(random.randrange(1, 10))
print(a)