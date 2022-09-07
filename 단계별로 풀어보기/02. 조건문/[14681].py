x = int(input())
y = int(input())

if x >= -1000 and x < 0 :
    if y >= -1000 and y < 0 :
        print(3)
    elif y <= 1000 :
        print(2)
elif x <= 1000 :
    if y >= -1000 and y < 0 :
        print(4)
    elif y <= 1000 :
        print(1)
        
# print("3421"[input()>"0"::2][input()>"0"]) 이해하기
