a = {
	'a': {
		'b': {
			'c': '+++'
        }
    },
}
def func(key : str, a):
    key = key.split(".")
    q = "a"
    for i in key:
        q = q + "[" + "'" + i + "'" +"]"
    q1 = eval(q)
    return q1

# print(eval(a["a"]["b"]["c"]))
print(func('a.b.c', a))