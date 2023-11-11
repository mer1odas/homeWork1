from datetime import date
import math

def fevral29():
    today = date.today()
    year_today = int(((str(today).split("-")))[0])
    year_end = date(year_today, 12, 31)
    year_end1 = int(((str(year_end - today)).split())[0])
    print(year_end1)
    year = (4 - year_today % 4)
    if year == 1:
        do_fevral_29 = year_end1 + 60
    else:
        do_fevral_29 = year_end1 + ((year - 1) * 365) + 60
    return do_fevral_29

print(fevral29())