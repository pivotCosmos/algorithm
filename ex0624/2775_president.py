import sys

# t = int(input())
# for i in range(t) :
#     k= int(input())
#     n = int(input())
#     if n == 1 :
#         print(1)
#     elif k == 0 :
#         print(n)
#     else :
#         oldList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # 0층
#         newList = []
#         for l in range(k) :
#             for j in range(n) :
#                 if j ==0 :
#                     newList.append(1)
#                 else :
#                     newList.append(newList[j-1] + oldList[j])
#             oldList = newList
#             newList = []
#         print(oldList[n-1])

t = int(input())
for i in range(t) :
    k= int(input()) # 층
    n = int(input()) # 호
    if n == 1 :
        print(1)
    elif k == 0 :
        print(n)
    else :
        oldList = [x for x in range(1,n)]
        for j in range(k) :
            newList = [x for x ]