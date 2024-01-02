a = [
	{
		"id": "1",
		"city": "city1",
		"country": "country1",
    },
	{
		"id": "2",
		"city": "city2",
		"country": "country1",
    },
	{
		"id": "3",
		"city": "city3",
		"country": "country2",
    }
]
id = [
	{
		"id": "1",
		"country": "country1",
    },
	{
		"id": "2",
		"country": "country2",
    },
	{
		"id": "3",
		"country": "country3",
    }
]
id_contr = {}
for i in id:
    id_contr[i["country"]] = i['id']
for i in a:
    i["country_id"] = id_contr[i["country"]]
    del i["country"]
print(a)