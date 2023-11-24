import random
file = open("txt.txt", "r+")
file_sod = file.read()
file_sod = file_sod.split("\n")
file.close()
file = open("txt.txt", "w")
file.seek(0)
for i in reversed(range(0, len(file_sod))):
    print(i)
    if i == 0:
        file.write(file_sod[i])
    else:
        stroka = file_sod[random.randrange(0, i + 1)]
        print("<<<<", stroka)
        file.write(stroka + "\n")
        file_sod.remove(stroka)