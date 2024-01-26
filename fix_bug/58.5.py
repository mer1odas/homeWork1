def func(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(func(1, 2))