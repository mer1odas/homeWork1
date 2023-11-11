def sek(sek):
    dct = {}
    # dct["day"] = round(sek / 86400)
    # if dct["day"] != 0:
    #     dct["hours"] = round(sek - (dct["day"] * 86400))
    #     if dct["hours"] != 0:
    #         dct["min"] = round(sek - (dct["hours"] * 3600))
    #         if dct["min"] != 0:
    #             dct["sek"] = round(sek - (dct["min"] * 60))
    # else:
    #     dct["hours"] = round(sek / 3600)
    #     if dct["hours"] == 0:
    #          dct["min"] = round(sek - dct["hours"] * 3600) 
    #          if dct["min"] == 0:
    #              dct["sek"] = round(sek - dct["min"] * 60) 
    #     else:
    dct["day"] = int(sek / 86400)
    if dct["day"] != 0:
        dct["hours"] = int((sek - (dct["day"] * 86400)) / 3600)
    else:
        dct["hours"] = round(sek / 3600)
    if dct["hours"] != 0:
         dct["min"] = int((sek - (dct["hours"] * 3600) - (dct["day"] * 86400)) / 60)
    else:
         dct["min"] = round(sek / 60)
    if dct["min"] != 0:
         dct["sek"] = int(sek - (dct["day"] * 86400) - (dct["hours"] * 3600) - (dct["min"] * 60))
    else:
        dct["sek"] = sek
    return dct
print(sek(1076399))