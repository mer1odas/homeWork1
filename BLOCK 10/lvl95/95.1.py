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

a=int(input())
func1(a)