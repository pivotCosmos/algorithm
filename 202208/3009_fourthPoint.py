xlist = []
ylist = []
for i in range(3) :
    a,b = map(int,input().split())
    xlist.append(a)
    ylist.append(b)
print(min(xlist, key=lambda x : xlist.count(x)), min(ylist, key=lambda x: ylist.count(x)))