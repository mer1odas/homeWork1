affairs = [
	{
		'date':  '2019-12-29',
		'event': 'name1',
	},
	{
		'date':  '2019-12-31',
		'event': 'name2',
	},
	{
		'date':  '2019-12-29',
		'event': 'name3',
	},
	{
		'date':  '2019-12-30',
		'event': 'name4',
	},
	{
		'date':  '2019-12-29',
		'event': 'name5',
	},
	{
		'date':  '2019-12-31',
		'event': 'name6',
	},
	{
		'date':  '2019-12-29',
		'event': 'name7',
	},
	{
		'date':  '2019-12-30',
		'event': 'name8',
	},
	{
		'date':  '2019-12-30',
		'event': 'name9',
	}
]
q = set()
for i in affairs:
    q.add(i["date"])
print(q)