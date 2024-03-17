import json

aa = [11,22,33,44,55]
#bb = {'tris':(3,'tris')}
f = open("10kl_progs/darbs_ar_faliem.txt","w")
json.dump((aa),f)
f.close()


f = open("10kl_progs/darbs_ar_failiem.txt", "r")
a = json.load(f)

print(a)
