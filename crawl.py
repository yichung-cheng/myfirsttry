import requests

r = requests.get("https://www.google.com.tw/")
if (r.status_code == 200):
    print("ok")
r.encoding = "utf-8"
print(r.text)