a, b, c = map(int, open(0).read().split())
if a >= 1 and a <= 6 and b >= 1 and b <= 6 and c >= 1 and c <= 6 :
    if a == b or a == c :
        if  a == b and a == c :
            print(10000 + a*1000)
        else :
            print(1000+a*100)
    elif b == c :
        print(1000+b*100)
    elif a > b and a > c :
        print(a*100)
    elif b > c :
        print(b*100)
    else :
        print(c*100)
        
#*_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])
