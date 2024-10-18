import json

aa = [11,22,33,44,55]
#bb = {'tris':(3,'tris')}
f = open("darbs_ar_faliem_JSON.txt","a")
json.dump((aa),f)
f.close()


f = open("darbs_ar_failiem_JSON.txt", "r")
a = json.load(f)

print(a)
