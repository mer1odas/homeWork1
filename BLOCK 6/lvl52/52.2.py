from datetime import date

def day(month, day):
    data = date(2023, month, day)
    if int(str(data - date.today()).split()[0]) > 0:
        return ((str(data - date.today()).split()[0]) + " осталось")
    else:
        return (str(date.today() - data).split()[0] + " прошло")
    
print(day(11, 3))