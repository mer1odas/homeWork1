#func(1, 'яблоко', 'яблока', 'яблок'); // выведет '1 яблоко'
def func(a : int, q : list):
    # b = [2, 3, 4]
    b = [5, 6, 7, 8, 9, 10]
    a = str(a)
    # print(a[len(a) - 2 : len(a)])
    # print(a[len(a) - 1])
    if 10 <= int(a[len(a) - 2 : len(a)]) < 15 or int(a[len(a) - 1]) in b:
        return q[2]
    else:
        if int(a[len(a) - 1]) == 1:
            return q[0]
        else:
            return q[1]
        
print(func(1, ['яблоко', 'яблока', 'яблок']))
print(func(2, ['яблоко', 'яблока', 'яблок']))
print(func(3, ['яблоко', 'яблока', 'яблок']))
print(func(4, ['яблоко', 'яблока', 'яблок']))
print(func(5, ['яблоко', 'яблока', 'яблок']))
print()
print(func(11, ['яблоко', 'яблока', 'яблок']))
print(func(12, ['яблоко', 'яблока', 'яблок']))
print(func(21, ['яблоко', 'яблока', 'яблок']))
print(func(23, ['яблоко', 'яблока', 'яблок']))
print()
print(func(1312, ['яблоко', 'яблока', 'яблок']))