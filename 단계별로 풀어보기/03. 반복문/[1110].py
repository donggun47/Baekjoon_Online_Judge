t = a = int(input())
counter = 0
while True :
    b = (a%10)*10 + (a//10 + a%10)%10
    counter += 1
    if t == b :
        break
    a=b

print(counter)


# := 할당과 테스트를 동시에
#a=n=int(input());c=1
#while(a:=a%10*10+a*11//10%10)-n:c+=1
#print(c)
