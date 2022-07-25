# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

num = int(input())
originalList = [x for x in range(1,num+1)]
tempList = []
resultList = []
for i in range(num) :
    tempList = list(map(int,str(originalList[i]))) #자릿수별로 분리해서 저장
   
    if len(tempList)<3:
        resultList.append(originalList[i])
    elif len(tempList)==3 :
        gap1 = tempList[0] - tempList[1]
        gap2 = tempList[1] - tempList[2]
        if gap1 == gap2 :
            resultList.append(originalList[i])
    elif len(tempList)==4 :
        gap1 = tempList[0] - tempList[1]
        gap2 = tempList[1] - tempList[2]
        gap3 = tempList[2] - tempList[3]
        if gap1 == gap2 == gap3:
            resultList.append(originalList[i])

print(len(resultList))
