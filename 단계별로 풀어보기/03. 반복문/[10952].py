a = b = 1
while a+b > 0 :
    a, b = map(int,input().split())
    if a> 0 and a<=10 and b> 0 and b<=10:
        print(a+b)
