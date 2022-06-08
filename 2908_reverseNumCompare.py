twoNum = input().split()
newList = []
for i in range(2) :
    newList.append(list(map(int,str(twoNum[i]))))
    newList[i] = list(reversed(newList[i]))
    newList[i] = ''.join(map(str,newList[i]))

if newList[0]>newList[1] :
    print(newList[0])
else :
    print(newList[1])