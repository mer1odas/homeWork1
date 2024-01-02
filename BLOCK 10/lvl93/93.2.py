import random
parol = ""
n = int(input())
for i in range(n - 1):
    parol = parol + chr(random.randrange(97, 123))
parol = parol + parol[len(parol) - 1].upper()
parol = parol.replace(parol[len(parol) - 2], "")
parol = parol + chr(random.randrange(32, 43))
print(parol)