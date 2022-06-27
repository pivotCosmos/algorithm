n = int(input())
m = int(input())

temp = []
for i in range (n, m+1) :
    if i != 1 :
        temp.append(i)
    for j in range (2, i) :
        if i%j == 0 :
            temp.remove(i)
            break
if len(temp) == 0 :
    print(-1)
else :
    print(sum(temp), temp[0], sep='\n')