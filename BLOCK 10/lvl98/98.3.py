import math

def sum_deleteli(a):
    a1 = []
    for i in range(1, round(math.sqrt(a)) + 1):
        if a % i == 0:
            a1.append(i)
            if a / i != i:
                a1.append(round(a / i))
    a1.sort()
    # a1.remove(a1[0])
    a1.remove(a1[len(a1) - 1])
    sum = 0
    for i in a1:
        sum += i
    return sum

n1 = int(input())
n2 = int(input())
for q1 in range(min(n1, n2), max(n1, n2) + 1):
    for q2 in range(min(n1, n2), max(n1, n2) + 1):
        if q1 == q2:
            continue
        sum_q1 = sum_deleteli(q1)
        sum_q2 = sum_deleteli(q2)
        if sum_q1 == q2 and sum_q2 == q1:
            print("Пара числе", q1, "и", q2, "являются дружественными")