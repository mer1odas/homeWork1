from datetime import date

def zodiak(month, day):
    data = date(2023, month, day)
    kozerog = date(2023, 1, 19)
    vodoley = date(2023, 2, 19)
    ribi = date(2023, 3, 20)
    oven = date(2023, 4, 19)
    telec = date(2023, 5, 20)
    blizneci = date(2023, 6, 20)
    rak = date(2023, 7, 22)
    lev = date(2023, 8, 22)
    deva = date(2023, 9, 22)
    vesi = date(2023, 10, 23)
    skorpion = date(2023, 11, 22)
    strelec = date(2023, 12, 21)
    kozerog1 = date(2023, 12, 31)
    if int((str(kozerog - data)).split()[0]) >= 0:
        return print("козерог")
    if int((str(vodoley - data)).split()[0]) >= 0:
        return print("водолей")
    if int((str(ribi - data)).split()[0]) >= 0:
        return print("рыбы")
    if int((str(oven - data)).split()[0]) >= 0:
        return print("овен")
    if int((str(telec - data)).split()[0]) >= 0:
        return print("телец")
    if int((str(blizneci - data)).split()[0]) >= 0:
        return print("близнецы")
    if int((str(rak - data)).split()[0]) >= 0:
        return print("рак")
    if int((str(lev - data)).split()[0])>= 0:
        return print("лев")
    if int((str(deva - data)).split()[0]) >= 0:
        return print("дева")
    if int((str(vesi - data)).split()[0]) >= 0:
        return print("весы")
    if int((str(skorpion - data)).split()[0]) >= 0:
        return print("скорпион")
    if int((str(strelec - data)).split()[0]) >= 0:
        return print("стрелец")
    if int((str(kozerog1 - data)).split()[0]) >= 0:
        return print("козерог")
    
zodiak(11, 3)
    
    