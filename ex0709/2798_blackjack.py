from itertools import combinations 

n,m = map(int,input().split())
li = list(map(int, input().split()))

temp = list(combinations(li, 3))
# print('temp = ', temp)
re = []
for i in range(len(temp)) :
    if sum(temp[i]) <= m :
        # print('temp[i] = ', temp[i], 'sum(temp[i]) = ', sum(temp[i]))
        re.append(temp[i])

retemp = list(map((lambda x: sum(x)), re))
print(max(retemp))