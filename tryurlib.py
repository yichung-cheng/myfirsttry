
'''from urllib.parse import urlparse
url = "https://www.youtube.com/watch?v=zmjWdd2ojEs"
o = urlparse(url)

print("scheme = {}".format(o.scheme))
print("netloc = {}".format(o.netloc))
print("port = {}".format(o.port))
print("path = {}".format(o.path))
print("query = {}".format(o.query))
'''
import requests
url = input()
r = input()
html = requests.get(url)
html.encoding = "utf - 8"
#print(html.text)
htmllist = html.text.splitlines()
for r in htmllist:
    print(r)  

