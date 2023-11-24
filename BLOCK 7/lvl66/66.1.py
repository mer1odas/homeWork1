file = open("txt.txt")
file1 = open("txt1.txt", "w")
file_sod = file.read()
a_set = set()
kaknibyt = {}
for i in file_sod:
    a_set.add(i)
for sim in a_set:
    file1.write(str(sim) + ": " +  str(file_sod.count(sim) / len(file_sod) * 100) + " ")
# file1 = open("txt1.txt", "r")
# file.write()