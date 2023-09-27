 
# 1-й вариант: 
 
a = int(input()) 
b = int(input()) 
c = int(input()) 
  
m = a 
if m < b: 
    m = b 
if m < c: 
    m = c 
  
print(m) 
 
# 2-й вариант: 
 
a = int(input()) 
b = int(input()) 
c = int(input())

if a > b: 
    if a > c: 
        print(a) 
    else: 
        print(c) 
else: 
    if b > c: 
        print(b) 
    else: 
        print(c) 