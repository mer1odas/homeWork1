import os

def remove(papka):
    for i in os.listdir(papka):
        os.remove(papka + "/" + i)
    os.removedirs(papka)

remove("files2")