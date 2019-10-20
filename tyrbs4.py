import requests
from bs4 import BeautifulSoup
import re
url = input()
html = requests.get(url)
html.encoding = "utf - 8"
sp = BeautifulSoup(html.text, 'html.parser')
#pat = re.compile('<td class=[a-z0-9A-Z]+'
print(sp.find_all('html'))