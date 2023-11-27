data = [
	{
		'year':  2019,
		'month': 11,
		'day': 20,
		'data': ['список с данными']
	},
	{
		'year':  2019,
		'month': 11,
		'day': 21,
		'data': ['список с данными']
	},
	{
		'year':  2019,
		'month': 12,
		'day': 25,
		'data': ['список с данными']
	},
	{
		'year':  2019,
		'month': 12,
		'day': 26,
		'data': ['список с данными']
	},
	{
		'year':  2020,
		'month': 10,
		'day': 29,
		'data': ['список с данными']
	},
	{
		'year':  2020,
		'month': 10,
		'day': 30,
		'data': ['список с данными']
	},
	{
		'year':  2020,
		'month': 11,
		'day': 19,
		'data': ['список с данными']
	},
	{
		'year':  2020,
		'month': 11,
		'day': 20,
		'data': ['список с данными']
	},
]
data1 = {}
for i in data:
    year = i["year"]
    month = i["month"]
    day = i["day"]
    data = i["data"]
    if year in data1:
        if month in data1[year]:
            data1[year][month][day] = data
        else:
            data1[year][month] = {day : data}
    else:
        data1[year] = {month : {day : data}}
print(data1)
                