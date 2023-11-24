a = ["files", "files1", "files2"]
b = input()
for i in a:
    open(b + "/" + i, "w")