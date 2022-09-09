H, M  = map(int,input().split())
timer = int(input())
if timer >= 0 and timer <= 1000 :
    print(f"{(H+int((M+timer)/60))%24} {(M+timer)%60}")
    
    
    
#h,m,t=map(int,open(0).read().split())
#m+=t
#print((h+m//60)%24,m%60)
