import random
a = "asbc"
q = []
for i in a:
    q.append(i)
a = ""
for i in range(len(q)):
    bykva = q[random.randrange(0, len(q))]
    a = a + bykva
    q.remove(bykva)
print(a)