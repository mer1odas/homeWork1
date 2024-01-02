txt = 'abcde abcde'
del1 = "abe"
for i in del1:
    for i1 in range(txt.count(i)):
        txt = txt.replace(i, "")
print(txt)