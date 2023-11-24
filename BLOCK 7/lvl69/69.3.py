import os

def file(pyt):
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
    return name

print(file("files"))