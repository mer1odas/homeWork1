from datetime import date
import math

def fevralvoskr():
    today = date.today()
    year_today = int(((str(today).split("-")))[0])
    year_end = date(year_today, 12, 31)
    year_end1 = int(((str(year_end - today)).split())[0])
    print(year_end1)
    do_fefral = year_end1 + 58
    return do_fefral

print(fevralvoskr())