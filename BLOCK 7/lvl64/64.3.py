a = input()
file = open("txt.txt")
file_sod = file.read()
if a in file_sod:
    print("есть")
else:
    print("нет")