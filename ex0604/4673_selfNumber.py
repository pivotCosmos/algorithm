#10000>=n>0

originalList = [x for x in range(1,10001)] #list comprehension

tempStrList = [] #분리된 숫자 저장
newList = [] #셀프넘버가 아닌 숫자 저장
for i in range(len(originalList)) :
    tempStrList = list(map(int,str(originalList[i])))
    newNum = originalList[i] + sum(tempStrList)
    newList.append(newNum)

#resultList = list(set(originalList)-set(newList)) #셀프넘버 저장
resultList = [x for x in originalList if x not in newList] #list comprehension
print(*sorted(resultList), sep="\n")
