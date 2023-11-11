def bykva(a):
    ord_a = ord(a)
    if ord_a >= 1040 and ord_a <= 1104:
        return "кирилица"
    if ord_a >= 65 and ord_a <= 122:
        return "латиница"
print(bykva("a"))
print(bykva("G"))
print(bykva("J"))
print(bykva("f"))
print(bykva("л"))
print(bykva("П"))
print(bykva("Й"))
print(bykva("ф"))
