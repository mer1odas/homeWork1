import os 
 
def size(pyt):
    return os.path.getsize(pyt)

print(size("txt.txt"))