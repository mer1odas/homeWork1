a = int(input())
i1 = 2
q = []
while a != 1:
    for i in range(2, a + 1):
        if a % i == 0:
            q.append(i)
            a = a // i
            break

b = ''
for i in q:
    b = b + str(i) + "*"
print(b[0 : len(b) - 1])