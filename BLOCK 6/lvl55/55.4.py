def dele(a, a1):
    q = []
    for i in range(min(a, a1), max(a, a1) + 1):
        q.append(i)
    return q

print(dele(1, 102))