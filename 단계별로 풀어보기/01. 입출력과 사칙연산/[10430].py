A, B, C = map(int,input().split())
play = []

numbercheck = [A, B, C]
for i in numbercheck :
    if i >= 2 and i <= 10000:
        play.append(i)
    else :
        break

if len(play) == 3 :
    print(f"{(A+B)%C} \n{((A%C) + (B%C))%C} \n{(A*B)%C} \n{((A%C) * (B%C))%C}")
    
A, B, C = map(int,input().split())
play = []

for i in [A,B,C] :
    if i >= 2 and i <= 10000:
        play.append(i)

if len(play) == 3 :
    print(f"{(A+B)%C} \n{((A%C) + (B%C))%C} \n{(A*B)%C} \n{((A%C) * (B%C))%C}")

# :=  연산자 공부하기
