import os
size = []
for i in os.listdir("files"):
    size.append(os.path.getsize("files/" + i))
print(size)