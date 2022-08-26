xlist = []
ylist = []
for i in range(3) :
    a,b = map(int,input().split())
    xlist.append(a)
    ylist.append(b)

# def findMinCount(array) :
#     counts = []
#     for i in range(len(array)) :
#         count = array.count(array[i])
#         counts.append(count)
#     index = counts.index(min(counts))
#     return array[index]

print(min(xlist, key=lambda x: xlist.count(x)), min(ylist, key=lambda x: ylist.count(x)))