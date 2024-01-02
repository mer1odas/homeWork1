def func(a : list, count):
    for i in a:
        print(type(i))
        if type(i) == list:
            print("123")
            count += 1
            count = func(i, count)
    return count

print(func([1, 2, [3, [4]]], 1))