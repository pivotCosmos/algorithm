# 최소공배수
import sys

N = int(input())
for i in range(N) :
    A, B = map(int, input().split())

    n1 = A
    n2 = B

    while n2 != 0 :
        temp = n1
        n1 = n2
        n2 = temp%n1

    print(A*B//n1)