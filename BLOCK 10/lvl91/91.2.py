import re
a = 'aaa bbb, ccc. Xxx - eee bbb, kkk!'
b = re.split(" |,|-|!", a)
for i in range(b.count("")):
    b.remove("")
print(b)