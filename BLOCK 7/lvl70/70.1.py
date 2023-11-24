file = open("txt.txt")
file_sod = file.read()
file_sod = file_sod.split("\n")
if file_sod[0] == "" and file_sod[len(file_sod) - 1] == "" and file_sod[len(file_sod) - 2] == "":
    print("файле в начале одна пустая строка, а в конце - две пустых строки.")