def stroka(a : str):
    a1 = ""
    a = a.split()
    for i in a:
        a1 = a1 +i[0].upper()
    return a1

print(stroka("asf, haha, fgdg"))