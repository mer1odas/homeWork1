file = open("txt.txt", "r+")
file_sod = file.read()
for i in file_sod:
    if i.isdigit():
        file.write(str(int(i) ** 2))