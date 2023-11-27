url = 'http://test.com/dir1/dir2/dir3/page.html'
print(url[url.find(".com/") + 5 : url.find("/dir2")])