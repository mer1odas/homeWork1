def data(data : str):
    data1 = data.split("-")
    year = data1[0]
    month = data1[1]
    day = data1[2]
    if int(year) < 0 or int(year) > 2023 or int(month) < 0 or int(month) > 12 or int(day) < 0 or int(day) > 31 or int(month) == 2 and int(day) > 29:
        return("неверная")
    else:
        return ("верная")
    
print(data("2021-2-21"))