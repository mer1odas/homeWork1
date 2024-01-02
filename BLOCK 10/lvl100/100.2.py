n = int(input())
n1 = int(input())
q = []
p = 2
for i in range(min(n, n1) + 2, max(n, n1) + 1):
    q.append(i)
print(q)
while p <= 7:
    for i in q:
        if i % p == 0 and i != p:
            q.remove(q[q.index(i)])
    print(q)
    p = q[q.index(p) + 1]
print(q)