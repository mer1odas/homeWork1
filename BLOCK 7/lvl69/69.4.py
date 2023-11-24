import os
name = []
podpapki = []
for i in os.listdir("files"):
    if os.path.isdir("files/" + i):
        podpapki.append(i)
    else:
        if ".png" in i:
            name.append(i)
for i1 in podpapki:
    for i2 in os.listdir("files/" + i1):
        if ".png" in i2:
            name.append(i2)
for i2 in name:
    open("files1/" + i2, "w")
    # os.replace("files/file/", i2)
print(name)