import os
q = []
for i in os.listdir("files"):
    if os.path.isdir("files/" + i):
        q.append(i)
print(q)
