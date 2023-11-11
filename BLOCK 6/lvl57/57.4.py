def func(lst : list, a):
    if lst.index(a) == len(lst) - 1:
        return lst[0]
    else:
        return lst[lst.index(a) + 1]

lst = [1, 2, 3, 4, 5]
print(func(lst, 1))
print((func(lst, 4)))
print(func(lst, 5))