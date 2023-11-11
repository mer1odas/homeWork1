def year():
    year = []
    for i in range(1923, 2023):
        if i % 4 == 0:
            year.append(i)
    return year

print(year())
        