# 방법1
# import sys

# N = int(input())
# li = []
# for i in range(N) :
#     temp = sys.stdin.readline().rstrip().split()
#     numTemp = [int(temp[0]),int(temp[1])]
#     li.append(numTemp)

# li.sort()

# for i in range(N) :
#     print(*li[i], sep=' ')


# 방법2
# import sys
# input = sys.stdin.readline # class 'builtin_function_or_method'
# n = int(input()) # builtin_function_or_method 사용할 때는 괄호를 붙인다.
# array = [list(map(int, input().split()))for _ in range(n)] # 언더스코어(_) : 값을 무시하고 싶을 때

# array = sorted(array, key=lambda x : (x[0], x[1])) # sorted() : key, reverse 매개변수 가진다. lambda를 이용해 여러개의 요소로 정렬

# for i in array:
#     print(' '.join(str(s) for s in i))


# # 방법3
import sys
N = int(input())       
nums = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
nums.sort()
for x, y in nums:
    print(x, y)