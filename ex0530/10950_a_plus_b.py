n = int(input())
temp = []
for i in range(n) :
    i,j=map(int,input().split())
    temp.append(i+j)
for i in range(len(temp)) :
    print(temp[i])