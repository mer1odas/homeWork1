a1 = int(input())
a2 = int(input())
result = ""
a1 = str(a1)
# a3 = int(a1)
i = 0
for q in range(len(a1)):
    a3 = 0
    if i > len(a1) - 1:
        break
    if int(a1[i]) >= a2 == 0:
        q1 = int(a1[i])
        while q1 % a2 == 0:
            q1 -= 1
            a3 += 1
        result = result + str(q // a2)
        # a3 -= int(a1[i] + ("0" * (len(a1) - 1 - i)))
        print("-", a1[i] + ("0" * (len(a1) - 1 - i)), "|", result)
        a1 = a1.replace(a1[i], str(a3))
    else:
        q = int(a1[i : i + 2])
        # print(q, "q")
        if q % a2 == 0:
            result = result + str(q // a2)
            # a3 -= int(a1[i : i + 2] + ("0" * (len(a1) - 2 - i)))
            print("-", a1[i : i + 2] + ("0" * (len(a1) - 2 - i)), "|", result)
            i += 2
        else:
            while q % a2 != 0:
                q -= 1
                a3 += 1
            result = result + str(q // a2)
            print("-", str(q) + ("0" * (len(a1) - 2 - i)), "|", result)
            # print(">>>>>>>>", a3)
            if i != len(a1) - 1:
                a1 = a1.replace(a1[i + 1], str(a3))
            i += 1



