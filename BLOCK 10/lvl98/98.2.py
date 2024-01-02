import random
import math
a = ["a", "b", "c", "d"]
q = []
q1 = []
for i in range(math.factorial(len(a))):
    # print(i)
    while q in q1:
        q = []
        for i1 in range(len(a)):
            index = random.randrange(0, len(a))
            while a[index] in q:
                index = random.randrange(0, len(a))
            q.append(a[index])
    q1.append(q)
    print(q)
    q = []