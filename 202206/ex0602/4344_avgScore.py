import sys

#평균 구하기
n = int(input())
avg = 0
for i in range(n) :
    l = list(map(int, sys.stdin.readline().split()))
    
    avg = sum(l[1:])/l[0]
    # #function
    # def isGtAvg(a) :
    #     if a > avg :
    #         return True
    #     return False

    #filter, lambda
    temp = len(list(filter(lambda n : n>avg, l[1:])))
    print("{0:0.3f}%".format(temp/l[0]*100))