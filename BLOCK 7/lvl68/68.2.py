import math
file = open("txt.txt")
file_sod = file.read()
file_sod = file_sod.split()
file_sod = set(file_sod)
file_sod = list(file_sod)
file.close()
file = open("txt1.txt", "r+")
# file_sod1 = file_sod.copy()
for i in range(math.ceil(len(file_sod) / 10)):
    for i1 in range(10):
        if len(file_sod) != 0:
            print(file_sod)
            file.write(file_sod[0] + " ")
            file_sod.remove(file_sod[0])
    file.write("\n")