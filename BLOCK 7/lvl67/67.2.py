import os
name = []
podpapki = []
for i in os.listdir("files"):
    if os.path.isdir("files/" + i):
        podpapki.append(i)
    else:
        name.append(i)
for i1 in podpapki:
    for i2 in os.listdir("files/" + i1):
        name.append(i2)
print(name)
