file = open("txt.txt")
a = file.read()
sum = 0
for i in a:
    if i.isalpha():
        sum += 1
print(sum)