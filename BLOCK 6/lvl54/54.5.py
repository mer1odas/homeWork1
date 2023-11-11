def dele(a):
    for i in str(a):
        if int(i) % 2 == 0:
            a = str(a).replace(i, "")
    return int(a)

print(dele(4441))
        