n = int(input())
re = []
for i in range(1, n) :
    temp = i
    templi = [int(x) for x in str(temp)]
    if temp + sum(templi) == n :
        re.append(temp)

if len(re) > 0 :
    print(min(re))
else :
    print(0)