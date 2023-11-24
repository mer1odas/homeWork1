import datetime
file = open("txt.txt", "r+")
file.write(str(datetime.datetime.now()))