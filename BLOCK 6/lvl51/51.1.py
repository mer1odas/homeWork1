from datetime import date

def today():
    weekdays = {0 : "Понедельник", 
                1 : "Вторник", 
                2 : "Среда", 
                3 : "Четверг", 
                4 : "Пятница", 
                5 : "Суббота", 
                6 : "Воскресенье"}
    return weekdays[date.today().weekday()]

print(today())
