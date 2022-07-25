import math
n = int(input())
m = n # 입력값 저장
s = 0 # 자릿수의 합
count = 0
while True :
    if count > 0 and n == m :
        break
    else :
        s = math.floor(n/10) + n%10
        n = (n%10)*10 + s%10
        count += 1
print(count)