import math

# def func(a):
#     a1 = []
#     for i in range(1, round(math.sqrt(a)) + 1):
#         if a % i == 0:
#             a1.append(i)
#             if a / i != i:
#                 a1.append(round(a / i))
#     a1.sort()
#     a1.remove(a1[0])
#     a1.remove(a1[len(a1) - 1])
#     return a1

# def func1(a):
#     mnojiteli = []
#     a1 = a
#     # for i in range(len(q)):
#     #     print(a, " " * (len(str(a1)) - len(str(a))) + "|", q[i])
#     #     a = int(a / q[i])
#     # print(a, " " * (len(str(a1)) - len(str(a))) + "|")
#     while a != 1:
#         for i in range(2, a1 + 1):
#             if a % i == 0:
#                 mnojiteli.append(i)
#                 print(a, " " * (len(str(a1)) - len(str(a))) + "|", i)
#                 a = int(a / i)
#     mnojiteli.sort()
#     return mnojiteli

def func1(a):
    a1 = a
    mnojiteli = []
    i = 2
    while a != 1:
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
# mnojit1 = func(a1)
# mnojit2 = func(a2)
q1 = func1(max(a1, a2))
print("\n")
q2 = func1(min(a1, a2))
# for i in mnojit1:
kratnoe = ""
kratnoe1 = 1
for i in q1:
    kratnoe = kratnoe + str(i) + "*"
    kratnoe1 *= i
for i1 in q2:
    if not(i1 in q1):
        kratnoe1 *= i1
        kratnoe = kratnoe + str(i) + "*"
print(kratnoe[0 : len(kratnoe) - 1], "=", kratnoe1)
