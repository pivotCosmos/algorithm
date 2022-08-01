n = int(input())
li = []
for i in range(n) :
    li.append(int(input()))
for j in range(len(li)) :
    for i in range(1, len(li)) :
        if li[i-1] > li[i] :
            temp = li[i-1]
            li[i-1] = li[i]
            li[i] = temp
print(*li,sep='\n')