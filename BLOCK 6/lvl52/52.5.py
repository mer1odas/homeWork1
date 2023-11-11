from datetime import date
import calendar
import math

def day():
    year = int((str(date.today()).split("-"))[0])
    month = int((str(date.today()).split("-"))[1])
    return math.fabs(int(str(date.today()).split("-")[2]) - int(calendar.monthrange(year, month)[1]))

print(day())