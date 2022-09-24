a = []

for i in range(b):
    f = int(input())
    a.append(f)
maximum = -1000000

for i in range(b) :
    c = a[i]
    if c >  maximum :
        maximum = c
        d = i+1

print(maximum, d)
#아니 비주얼에선 정상작동인데 왜 nameerror임?
