n = int(input());
A = list(map(int,input().split()));
A2 = [A[0]];
v1 = 0;
n1 = 0;
val1 = 0;
f1 = 0;
f2 = 0;
val2 = 0;
kol = 0;
for i in range (1,n):
      if(A[i-1] == A[i]):
            v1+=1;
 
if (v1 == n-1):
      print(n-1);
else:
      
      for i in range (1,n):
            if (A[i-1 ] != A[i]):
                  A2.append(A[i]);
            else:
                  val2+=1;
 
      n1 = len(A2);
      for i in range (1,n1):
            if (A2[i-1] < A2[i])and(f1 == 0):
 
                  f2 = 0;
                  f1 = 1;
                  kol+=1;
         
            else:
                  if (f2 == 0)and(A2[i-1]>A2[i]):
          
                        f2 = 1;
                        f1 = 0;
                        kol+=1;
      
 
      print(n-kol-1);
        
