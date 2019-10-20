import re
pat = re.compile('http://[a-zA-Z0-9./_@]+')
ip = input()
m = pat.findall(ip)
print(m)