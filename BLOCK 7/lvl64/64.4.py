import os
a = input()
file = open("txt.txt", "r+")
for i in os.listdir("files"):
    file1 = open("files/" + i)
    file1 = file1.readlines()
    file1 = (file1[0 : int(a)])
    for i1 in file1:
        print(i1)
        file.write(i1)
    