#deklarējot veselu skaitļu sarakstu

#numList =[10,9,2,3,1,4,5,8,7,3.2,3.5,3.1]

#numList=input().split() - 1.solis

#numList=map(int,input().split()) - 2.solis

numList=list(map(float,input().split())) # - 3.solis

#sākotnējā saraksta drukāšana
print("Sākotnējais saraksts ir:")
print(numList)
# saraksta kārtošana augošā secībā
numList.sort()
# augošā secībā sasortā saraksta drukāšana
print("sortais saraksts augošā secībā:")
print(numList)
# saraksta kārtošana augošā secībā
numList.sort(reverse=True)
# dilstošā secībā sasortā saraksta drukāšana
print("sortais saraksts dilstošā secībā:")
print(numList)
