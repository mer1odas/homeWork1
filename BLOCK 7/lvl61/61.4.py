file = open("txt.txt", "r+")
slova = file.read()
slova = slova.split()
stroka = ""
for i in slova:
    if i == "1/2":
        stroka = stroka + "(" + i + ")" + " "
    else:
        stroka = stroka +  i + " "
file1 = open("txt2.txt", "w")
file1.write(str(stroka))