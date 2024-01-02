for i in range(2000, 2024):
    for i1 in range(1, 13):
        for i2 in range(1, 32):
            if (str(i) + str(i1) + str(i2)).count("2") == 4:
                print(str(i) + "." + str(i1) + "." + str(i2))