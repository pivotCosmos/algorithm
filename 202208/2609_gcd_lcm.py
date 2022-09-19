# 최대공약수, 최소공배수 구하기
N, M = map(int, input().split())
 
n1 = N
n2 = M
#GCD
while n2!=0:
    temp = n1
    n1 = n2
    n2 = temp%n2
print(n1)

#LCM
print(N*M//n1)