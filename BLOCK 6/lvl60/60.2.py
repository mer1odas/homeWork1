import random

def ran_list(a):
    random.shuffle(a)
    # a1 = []
    # for i in range(len(a)):
    #         a1.append(a[random.randrange(0, len(a))])
    return a

print(ran_list([1, 2, 3, 5, 6, 7]))