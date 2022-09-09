H, M  = map(int,input().split())
if H >= 0 and H <= 23 :
    if M >= 0 and M <= 59 :
        M = M - 45
        if M < 0 :
            H = H -1
            M += 60
            if H < 0 :
                H = 23
print(f"{H} {M}")

#a,b=map(int,input().split())
#print((a-(b<45))%24,(b-45)%60) 공부하기
