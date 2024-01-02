import math
import random
x1 = 0.1
x2 = 0.1
while type(x1) != int and type(x2) != int:  
    a = random.randrange(-100, 100)
    b = random.randrange(-100, 100)
    c = random.randrange(-100, 100)
    while a == 0:
        a = random.randrange(-100, 100)
    D = b ** 2 - (4 * a * c)
    if D < 0:
        continue
    else:
        if D == 0:
            continue
        else:
            x1 = (-1 * b - math.sqrt(D)) / (2 * a)
            x2 = (-1 * b + math.sqrt(D)) / (2 * a)
            print(x1,x2)
            q1 = str(x1).split(".")
            q2 = str(x2).split(".")
            # print(q1)
            # print(q2)
            if q1[1] == "0" and q2[1] == "0":
                x1 = int(x1)
                x2 = int(x2)
                # print(type(x1), type(x2))
            # quit()

print(a, b, c)