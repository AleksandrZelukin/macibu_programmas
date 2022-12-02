import requests
import json

#Get data
result = requests.get("http://universities.hipolabs.com/search?country=latvia")
universities = json.loads(result.content)
uni_list = []
for uni in universities:
    uni_list.append(uni['name'])
uni_list = list(dict.fromkeys(uni_list))

#sort

uni_list.sort()

#print

for uni in uni_list:
    print(uni)