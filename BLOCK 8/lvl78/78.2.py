events = [
						{
		'date':  '2019-12',
		'event': 'name1'
	},
	{
		'date':  '2019-12',
		'event': 'name2'
	},
	{
		'date':  '2019-11',
		'event': 'name3'
	},
	{
		'date':  '2019-11',
		'event': 'name4'
	},
	{
		'date':  '2020-10',
		'event': 'name5'
	},
	{
		'date':  '2020-10',
		'event': 'name6'
	},
	{
		'date':  '2020-11',
		'event': 'name5'
	},
	{
		'date':  '2020-11',
		'event': 'name6'
	},
	{
		'date':  '2020-12',
		'event': 'name7'
	},
	{
		'date':  '2020-12',
		'event': 'name8'
	},
	{
		'date':  '2020-12',
		'event': 'name9'
	},
]
events_data = {}
for i in events:
    for i1 in i:
        if i1 == "date":
            year = i[i1][0 : 4]
            month = i[i1][5 : len(i[i1])]
        else:
            event = i[i1]
    if year in events_data:
        # print(events_data)
        if month in events_data[year]:
            events_data[year][month] = events_data[year][month] + ", " + event
        else:
            events_data[year][month] = event
    else:
        # print("year")
        events_data[year] = {month : event}
print(events_data)