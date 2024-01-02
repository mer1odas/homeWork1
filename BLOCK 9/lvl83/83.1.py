import random
a = ["gasd", "agsd", "agdsa"]
q = input()
slovo = a[random.randrange(0, len(a))]
while slovo[0] != q:
    slovo = a[random.randrange(0, len(a))]
print(slovo)
