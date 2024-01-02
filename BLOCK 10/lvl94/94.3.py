import math
# def func(a):
#     a1 = a
#     mnojiteli = []
#     for i in range(2, a1 + 1):
#             if a % i == 0:
#                 mnojiteli.append(i)
#                 print(a, " " * (len(str(a1)) - len(str(a))) + "|", i)
#                 a = int(a / i)
                # return mnojiteli, a
def func1(a):
    a1 = a
    mnojiteli = []
    i = 2
    while a != 1:
        # for i in range(2, a1 + 1):
        if a % i == 0:
            mnojiteli.append(i)
            print(a, " " * (len(str(a1)) - len(str(a))) + "|", i)
            a = int(a / i)
            i = 2
        else:
            i += 1
    print("1", " " * (len(str(a1)) - len(str(a))) + "|")
    mnojiteli.sort()
    return mnojiteli
        
a1 = int(input())
a2 = int(input())
q1 = func1(max(a1, a2))
print("\n")
q2 = func1(min(a1, a2))
delitel = ""
delitel1 = 1
for i in q2:
    if i in q1:
        delitel = delitel + str(i) + "*"
        delitel1 *= i
print(delitel[0 : len(delitel) - 1], "=", delitel1)

