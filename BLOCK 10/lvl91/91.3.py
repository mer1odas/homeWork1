a1 = 20
a2 = 123
sum1 = 0
for i in range(len(str(a2))):
    dobit = "0" * (len(str(a2)) - i - 1)
    dobit1 = "0" * i
    cifra = int(str(a2)[len(str(a2)) - 1 - i]) * a1
    print(dobit + str(cifra) + dobit1)
    sum1 += int(dobit + str(cifra) + dobit1)
print(sum1)
