import datetime
file = open("txt.txt", "r")
file_sod = file.read()
file.close()
file = open("txt.txt", "w")
file.seek(0)
file.close()
file = open("txt.txt", "r+")
file.write(str(datetime.datetime.now()) + str(file_sod))