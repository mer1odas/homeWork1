import random
file = open('txt.txt')
file_sod = file.read()
file_sod = file_sod.split(".")
print(file_sod)
file1 = open("txt1.txt", "r+")
for i in file_sod:
    i = i.split()
    print(i)
    for i1 in range(len(i)):
        slovo = i[random.randrange(0, len(i))]
        file1.write(slovo + " ")
        i.remove(slovo)
    file1.write(". ")