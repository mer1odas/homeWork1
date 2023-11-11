from datetime import date

def day():
    days = {}
    weekdays = {0 : "Понедельник", 1 : "Вторник", 2 : "Среда", 3 : "Четверг", 4 : "Пятница", 5 : "Суббота", 6 : "Воскресенье"}
    days["next"] = weekdays[date.today().weekday() + 1]
    days["curr"] = weekdays[date.today().weekday()]
    days["prev"] = weekdays[date.today().weekday() - 1]
    return days

print(day())