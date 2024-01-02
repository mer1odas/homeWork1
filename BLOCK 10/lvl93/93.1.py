import random
a = (7, 7, 1, 0, 8, 7)
a1 = list(a)

def func(a : list):
    a1 = a.copy()
    q = ""
    for i in range(len(a)):
        cifra = a1[random.randrange(0, len(a1))]
        q = q + str(cifra)
        a1.remove(cifra)
    return q

bilet = func(a1)
while int(bilet[0]) + int(bilet[1]) + int(bilet[2]) != int(bilet[3]) + int(bilet[4]) + int(bilet[5]):
    bilet = func(a1)
print(bilet, ">>>")

