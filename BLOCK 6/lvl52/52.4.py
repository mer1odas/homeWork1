def year(year):
    if year % 4 == 0:
        return "високосный"
    else:
        return "невисоскосный"
    
print(year(2000))
