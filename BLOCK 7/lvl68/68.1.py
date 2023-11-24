import random
file = open("txt.txt", "r+")
file_sod = file.read()
file.close()
file = open("txt.txt", "w")
file.seek(0)
file_sod = file_sod.split()
print(file_sod)
for i in range(len(file_sod)):
    slovo = file_sod[random.randrange(0, len(file_sod))]
    file.write(slovo + " ")
    file_sod.remove(slovo)
    
