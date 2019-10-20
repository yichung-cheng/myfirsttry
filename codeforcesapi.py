import requests
import bs4
import json
url = "https://codeforces.com/api/problemset.problems?tags=implementation"
theget = requests.get(url)
text = json.loads(theget.text)
thetags = input()
for i in range(len(text["result"]["problems"])):
    flag = False
    for j in range(len(text["result"]["problems"][i]["tags"])):
        if(text["result"]["problems"][i]["tags"][j] == thetags):
            flag = True
            break
    if(flag):
        print(text["result"]["problems"][i]["name"])