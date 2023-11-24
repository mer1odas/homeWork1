a = [1, 2, 3, 4, 5]
file = open("txt.txt", "r+")
for i in a:
    file.write(str(i) + "\n")