import os
a = input()
for i in os.listdir("files"):
    tip_file = (os.path.splitext(i))[1]
    if tip_file == a:
        os.remove("files/" + i)