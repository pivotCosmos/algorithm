sixList = [1]
n = int(input())
i = 1
while n > sum(sixList) : # 7 , 1+6 / 13 , 1+6+12 / 17, 1+6+12 / 37, 1+6+12+18
    sixList.append(6*i)
    i = i + 1
    # print('sixList =',sixList,'i =',i)
print(i)