import sys
n = int(input())
alphabetList = 'abcdefghijklmnopqrstuvwxyz'
result = n
for i in range(n) :
    word = sys.stdin.readline().rstrip()
    temp = 0

    for a in alphabetList :
        #개수 구하기
        temp = list(word).count(a)
        # print('temp =', temp)
        if temp > 1 :
            #첫번째 위치 찾기
            startIndex = word.find(a)
            # print('startIndex = ',startIndex)
            #마지막 위치 찾기
            endIndex = word.rfind(a)
            # print('endtIndex = ', endIndex)
            #위치 차이+1이 개수와 같지 않으면 result에서 제외
            if temp != endIndex - startIndex + 1:
                result = result - 1
                break
                #print('result =',result)
print(result)
