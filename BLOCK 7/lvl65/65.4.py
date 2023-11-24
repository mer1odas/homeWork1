file = open("txt.txt")
file_sod = file.read()
file.close()
# for i in range(file_sod.count(" ")):   
# file_sod.replace(" ", "-", file_sod.count(" "))
a = ""
file_sod = file_sod.split(" ")
for i in file_sod:
    a = a + i + "-"
file1 = open("txt1.txt", "w")
file1.write(a[0 : len(a) - 1])