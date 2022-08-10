import sys
N = int(input())
numbers = list(map(int,sys.stdin.readline().split()))
numberSet = set(numbers) # 중복제거
sortedNumbers = sorted(list(numberSet)) # 정렬
results = []
for i in range(N) :
    results.append(sortedNumbers.index(numbers[i]))
print(sortedNumbers)
print(results)