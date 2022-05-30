n = int(input())

# if n%2==0 :#짝수일때
#     print(int((1+n)*(n/2)))
# else :#홀수일때
#     print(int((1+n)*(n//2)+(n/2+0.5)))

#반복문 사용
i = 1
temp = 0
while i <= n:
    temp = temp + i
    i = i + 1
print(temp)

