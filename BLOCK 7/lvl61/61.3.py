file = open("txt.txt", "r+")
slova = file.read()
slova = slova.split()
stroka = ""
for i in slova:
     stroka = stroka + "(" + i + ")"
     print(stroka)
file1 = open("txt1.txt", "w")
file1.write(str(stroka))