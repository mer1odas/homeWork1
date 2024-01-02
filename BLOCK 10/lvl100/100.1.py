a = '8/10'
a1 = a.split("/")
b = int(a1[0])
c = int(a1[1])
q = -1

def func(b, c):
    q = 1
    while True:
        if q > min(c, b):
            q = 0
            return q
        q += 1
        if b % q == 0 and c % q == 0:
            return q

while q < min(c, b):
    q = func(b, c)
    if q  == 0:
        print(a)
        break
    a = a + " = " + str(b // q) + "/" + str(c // q)
    b = b // q
    c = c // q