import sys

T = int(sys.stdin.readline())
for i in range(T) :
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)
    
#for l in[*open(0)][1:]:print(sum(map(int,l.split()))) 이거 왜 실행되는 거임?
