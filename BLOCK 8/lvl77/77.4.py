import random
events = {
	'2019-12-29': ['name1', 'name3', 'name5', 'name7'],
	'2019-12-30': ['name4', 'name8', 'name9'],
	'2019-12-31': ['name2', 'name6'],
}
events1 = []
for i in events:
    for i1 in events[i]:
        events1.append({"date" : i,
                        "event" : i1})
events2 = []
for i in range(len(events1)):
    chislo = random.randrange(0, len(events1))
    events2.append(events1[chislo])
    events1.remove(events1[chislo])
print(events2)