file = open("txt.txt")
file_sod = file.read()
file_sod = file_sod.split(".")
for i in file_sod:
    if i[0].islower():
        print("Есть маленькая")