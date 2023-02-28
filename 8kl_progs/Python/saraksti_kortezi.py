aa = [45,6,78,16,34,56,4]

aa.append(34)
aa.insert(2,45)

bb = aa.pop()
bb = aa.pop(0)
aa.remove(16)

del aa[0:6:2]

print(aa)
bb=[45,6,78,16,34,56,4]
dd = aa+bb
print(dd)