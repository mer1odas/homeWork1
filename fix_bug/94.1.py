import re
import random

a = "dfsauuyg vevgfds hh rhr hrth rhtr, hrhgrth ,htr hrhrh  hrhtr h"
a = re.split(",| ", a)
for i in range(a.count("")):
    a.remove("")

b = ''
q = a.copy()
for i in range(len(q)):
    rand = random.randrange(0, len(a))
    b = b + a[rand] + " "
    a.remove(a[rand])

print(b)