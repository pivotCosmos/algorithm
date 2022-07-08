# 브루트 포스
n,m = map(int,input().split())
li = list(map(int, input().split()))
temp = []
for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            if i != j and j != k and i != k :
                temp.append([li[i],li[j],li[k]])
sums = []
for i in range(len(temp)) :
    s = sum(temp[i])
    if s <= m :
        sums.append(sum(temp[i]))

print(max(sums))

# from itertools import combinations 

# n,m = map(int,input().split())
# li = list(map(int, input().split()))

# temp = list(combinations(li, 3))
# # print('temp = ', temp)
# re = []
# for i in range(len(temp)) :
#     if sum(temp[i]) <= m :
#         # print('temp[i] = ', temp[i], 'sum(temp[i]) = ', sum(temp[i]))
#         re.append(temp[i])

# retemp = list(map((lambda x: sum(x)), re))
# print(max(retemp))