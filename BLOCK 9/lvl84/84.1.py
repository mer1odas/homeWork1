url = 'http://test.com/dir1/dir2/dir3/page.html'
q = []
q.append(url[url.find(".com") + 4 : url.find("/page")])
q.append(q[0][0 : 10])
q.append(q[1][0 : 5])
print(q)