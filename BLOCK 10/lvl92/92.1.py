import math
a = int(input())
b = int(input())
c = int(input())
D = b ** 2 - (4 * a * c)
print(D)
if D < 0:
    print("Корней нет")
    quit()
else:
    if D == 0:
        print(-(b / 2 * a))
    else:
        x1 = (-1 * b - math.sqrt(D)) / (2 * a)
        x2 = (-1 * b + math.sqrt(D)) / (2 * a)
        print(x1, x2)