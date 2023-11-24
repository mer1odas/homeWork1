file = open("txt.txt")
file_cod = file.read()
file_cod = file_cod.split(",")
int_file_cod = []
for i in file_cod:
    int_file_cod.append(int(i))
print(max(int_file_cod))