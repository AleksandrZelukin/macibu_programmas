a = int(input())

f = open("darbsArFailiem_8a.txt","a")
print(a,file=f)

f.close()
'''
s = open("darbsArFailiem_8a.txt","r").readlines()
print(s)
'''

for i in open("darbsArFailiem_8a.txt","r",encoding="utf-8"):
    print(i)
