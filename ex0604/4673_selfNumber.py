#10000>=n>0

originalList = [x for x in range(1,10001)] #list comprehension

#newList = [x for x in originalList if x+ in originalList]

tempStrList = []
newList = []
for i in range(len(originalList)) :
    tempStrList = list(map(int,str(originalList[i])))
    newNum = originalList[i] + sum(tempStrList)
    newList.append(newNum)

resultList = list(set(originalList)-set(newList))
print(*sorted(resultList), sep="\n")
