import random

def cvet():
    cvet = {
        0 : "красный",
        1 : "синий",
        2 : "фиолетовый",
        3: "зеленый", 
        4 : "желтый",
        5 : "черный",
        6 : "белый"}
    return cvet[random.randrange(0, 6 + 1)]

print(cvet())