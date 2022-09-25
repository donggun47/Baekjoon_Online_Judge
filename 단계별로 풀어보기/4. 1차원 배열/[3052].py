a = []
result=[]
for i in range(10):
    a.append(int(input()))

for value in a:
    if value%42 not in result:
        result.append(value%42)

print(len(result))
