url = 'http://test.com/dir1/dir2/dir3/page.html'
num = 2
val = 'eee'
pos1 = url.find(str(num)) - 3
pos2 = url.find(str(num)) + 1
url = url.replace(url[pos1 : pos2], val)
print(url)