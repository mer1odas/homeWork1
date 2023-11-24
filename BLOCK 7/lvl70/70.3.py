import os 
print(os.path.abspath("txt.txt"))
pyt = "files"
name = []
podpapki = []
for i in os.listdir(pyt):
    if os.path.isdir(pyt + "/" + i):
        podpapki.append(i)
    else:
        name.append(i)
for i1 in podpapki:
    for i2 in os.listdir(pyt + "/" + i1):
        name.append(i2)

file1 = open("txt1.txt", "w")
for i2 in name:
    file1.write(os.path.abspath(i2) + "\n")
