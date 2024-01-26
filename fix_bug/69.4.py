import os
name = []
podpapki = []
for i in os.listdir("filess"):
    if os.path.isdir("filess/" + i):
        podpapki.append(i)
    else:
        if ".png" in i:
            name.append(i)
for i1 in podpapki:
    for i2 in os.listdir("filess/" + i1):
        if ".png" in i2:
            name.append(i2)
for i2 in name:
    open("filess1/" + i2, "w")
    # os.replace("files/file/", i2)
print(name)