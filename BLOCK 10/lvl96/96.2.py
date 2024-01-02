a = "))(("
a1 = a[:]
if a.count("(") == a.count(")"):
    for i in range(a1.count("(")):
        q = a.find("(")
        q1 = a[q : len(a)].find(")")
        if q1 < 0:
            print("-")
            break
        else:
            q1 += q            
            a = a.replace(a[q], "", 1)
            a = a.replace(a[q1 - 1], "", 1)
    if len(a) == 0:
        print("корректно")
else:
    print("-")