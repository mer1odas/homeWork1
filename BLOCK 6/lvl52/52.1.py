def delnoli(a):
    # while "0" in str(a):
    #     str(a).remove("0")
    for i in range(str(a).count("0")):
        a = str(a).replace("0", "")
    return str(a)

print(delnoli(500))
