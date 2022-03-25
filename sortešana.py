a=[34,12,1,56,4,17,2,90,5]
print(a)
a2=sorted(a)
print(a2)
a2=sorted(a,reverse=True)
print(a2)

a.sort()
print(a)
a.sort(reverse=True)
print(a)


aa=["one","twings","three","four"]
aa2=sorted(aa,key=len)
aa3=sorted(aa,key=len,reverse=True)
print(aa2)
print(aa3)

def myrev(s):
    return s[: : -1]

print([myrev(s) for s in aa])
aa2=sorted(aa, key=myrev)
print(aa2)

