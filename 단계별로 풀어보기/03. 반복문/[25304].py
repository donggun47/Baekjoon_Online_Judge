total = int(input())

ct = int(input())

ftotal = 0

for i in range(ct) :
    a, b =map(int,input().split())
    ftotal += a*b 

if ftotal == total :
    print("Yes")
else :
    print("No")
    
#X,N,*A=open(0)
#print("YNeos"[int(X)!=sum(eval(i.replace(*' *'))for i in A)::2])
