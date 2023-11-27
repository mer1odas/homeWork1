url = 'http://test.com/dir1/dir2/dir3/page.html'
url = url[url.find("com/") + 4 : url.find("/page")]
url = url.split("/")
print(url)