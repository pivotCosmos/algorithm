import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(n) :
    temp = 0
    if numbers[i] != 1 :
        for j in range(2, numbers[i]) :
            if numbers[i]%j == 0 :
                temp = temp + 1
                break
        if temp == 0 :    
            result = result + 1
print(result)