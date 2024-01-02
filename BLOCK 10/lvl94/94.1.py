import re
a = "dfsauuyg. vevgfds hh rhr. hrth rhtr, hrhgrth ,htr hrhrh  hrhtr h."
a = re.split(",| ", a)
for i in range(a.count("")):
    a.remove("")
print(a)