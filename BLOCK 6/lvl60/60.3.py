a = "ags ajhg aghd uyrh iutkhg asfasjhrh"
dct = {}
a1 = a.split()
# for i in range(65, 91):
#     print(chr(i))
#     for i1 in a1:
#         if i1[0] == chr(i):
#             dct[chr(i)] == i1
for i in range(97, 122):
    q = ""
    for i1 in a1:
        if i1[0] == chr(i):
            q = q + i1 + " "
            dct[chr(i)] = q
print(dct)
