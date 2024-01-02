parol = ""
count = 0
spec = ['/', '.', '!', '?']
if len(parol) > 8:
    count += 1
for i1 in spec:
    if i1 in parol:
            count += 1
            break
for i in parol:
    if i.isupper():
        count += 1
for i in parol:
    if i.islower():
        count += 1
        break
for i in parol:
    if i.isdigit():
        count += 1
        break

print(count)