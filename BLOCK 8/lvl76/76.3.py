events = [
	{
		'date': '2019-12-29',
		'event': 'name1'
	},
	{
		'date':  '2019-12-31',
		'event': 'name2'
	},
	{
		'date':  '2019-12-29',
		'event': 'name3'
	},
	{
		'date':  '2019-12-30',
		'event': 'name4'
	},
	{
		'date':  '2019-12-29',
		'event': 'name5'
	},
	{
		'date':  '2019-12-31',
		'event': 'name6'
	},
	{
		'date':  '2019-12-29',
		'event': 'name7'
	},
	{
		'date':  '2019-12-30',
		'event': 'name8'
	},
	{
		'date':  '2019-12-30',
		'event': 'name9'
	},
]
data = {}
proverka = 0
for i in events:
    for i1 in i:
        if proverka == 0:
            date = i[i1]
            proverka += 1
        else:
            event = i[i1]
            proverka = 0
    # strani.append({counter : sity})
    if date in data:
        data[date] = data[date] + ", " + event
    else:
         data[date] = event
print(data)