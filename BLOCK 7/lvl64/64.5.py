import os
for i in os.listdir("files"):
    file = open("files/" + i, "w+")
    file.seek(0)