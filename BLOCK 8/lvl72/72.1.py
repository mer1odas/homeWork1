url = 'http://test.com/dir1/dir2/dir3/page.html'
print(url[url.find("dir3/") + 5 : len(url)])