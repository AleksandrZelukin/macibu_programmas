import json
while True:
    a = input()
    f = open("darbs_ar_failiem.txt","w")
    json.dump(a,f)
    print(a, file=f)
    f.close()
    if a =="beigas":
        break
