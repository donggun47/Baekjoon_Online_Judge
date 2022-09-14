T = int(input())

for i in range(T) :
    a, b = map(int,input().split())
    print(f"Case #{i+1}: {a} + {b} = {a + b}")
    
#for i in [*open(0)][i:]:
#    a, b = map(int,input().split())
#    print(f"Case #{i+1}: {a} + {b} = {a+b}") 이거 왜 안되는지 이해하기

#i=0
#for a,_,c,_ in[*open(0)][1:]:i+=1;print(f'Case #{i}:',a,'+',c,'=',int(a)+int(c)) 이거 이해하기
