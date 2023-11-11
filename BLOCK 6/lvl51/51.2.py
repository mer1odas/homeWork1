from datetime import date

def weekday(year, month, day):
    data = date(year, month, day)
    weekdays = {0 : "Понедельник", 1 : "Вторник", 2 : "Среда", 3 : "Четверг", 4 : "Пятница", 5 : "Суббота", 6 : "Воскресенье"}
    return weekdays[data.weekday()]

print(weekday(2023, 11, 2))
