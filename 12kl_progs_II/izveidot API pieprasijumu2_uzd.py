from string import punctuation
spec_simboli = set(punctuation)
faila_saturs = []
with open('teksts.txt','r',encoding="utf8") as f:
    faila_saturs = f.readlines()
teikums = faila_saturs[0]
for simbols in spec_simboli:
    teikums = teikums.replace(simbols, " ")
vardu_masivs = teikums.split(" ")
for vards in vardu_masivs[:]:
    if len(vards) <4:
        vardu_masivs.remove(vards)
vardu_skaits = {}
for vards in vardu_masivs:
    vardu_skaits[vards] = vardu_masivs.count(vards)
sakaartots = sorted(vardu_skaits, key=vardu_skaits.get, reverse=True)
print("Vārds : atkārtošanās reizes")
for key in sakaartots[:5]:
    print(key, " : ", vardu_skaits[key])
