dd = [12,23,34,45,56,67,78,89]
ee = [25,37,48,59,60]

rr = []
ff = list()
rr.append('Latvija')
ff.append('Daugavpils')
rr.insert(0,'Talsi')
print(rr, ff)
print(dd,ee)
del dd[0]
dd.remove(78)
rr.remove('Talsi')
print(rr)