data = [
	{
		'country': 'country1',
		'city':    'city11',
	},
	{
		'country': 'country2',
		'city':    'city21',
	},
	{
		'country': 'country3',
		'city':    'city31',
	},
	{
		'country': 'country1',
		'city':    'city12',
	},
	{
		'country': 'country1',
		'city':    'city13',
	},
	{
		'country': 'country2',
		'city':    'city22',
	},
	{
		'country': 'country3',
		'city':    'city31',
	},
]
strani = {} #{"country1" : , 
#           "country2" : ,
#           "country3" : }
proverka = 0
for i in data:
    for i1 in i:
        if proverka == 0:
            counter = i[i1]
            proverka += 1
        else:
            sity = i[i1]
            proverka = 0
    # strani.append({counter : sity})
    if counter in strani:
        strani[counter] = strani[counter] + ", " + sity
    else:
         strani[counter] = sity
print(strani)