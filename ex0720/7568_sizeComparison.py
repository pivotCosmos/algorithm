n = int(input())
li = [] # 체격 정보
re = [] # 덩치 큰 순위
for i in range(n) :
    li.append(list(map(int, input().split())))

re = [len(li)]*len(li)
count = 0
for i in range(len(li)) : # 수를 하나 정하기
    for j in range(len(li)) : # 모든 경우의 수와 비교
        if j != i :
            if li[i][0] > li[j][0] and li[i][1] > li[j][1] :
                re[i] -= 1
            elif li[i][0] >= li[j][0] or li[i][1] >= li[j][1] :
                count += 1
    re[i] -= count
    count = 0

print(*re, sep=' ')