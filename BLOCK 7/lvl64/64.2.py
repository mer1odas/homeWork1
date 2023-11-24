import os
for i in os.listdir("files"):
    tip_file = (os.path.splitext(i))[1]
    if tip_file == ".png":
        print((os.path.splitext(i))[0])