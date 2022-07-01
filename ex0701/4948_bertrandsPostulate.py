import sys

# 소수만 저장하기
# resultSet = {x for x in range(2, 123456*2+1)}
# for i in range(2, int((123456*2)**0.5)+1) :
#             for j in range(i+i, 123456*2+1, i) :
#                 resultSet.discard(j)

# 범위 내의 모든 숫자에 대해 소수인지 아닌지 한번만 저장하기
N = 123456*2 + 1 # list는 [0]부터 시작하는데 [1]부터 사용할거니까 1을 더한다.
sieve = [True]*N
for i in range(2, int(N**0.5)+1) :
    if sieve[i]:
        for j in range(i*2, N+1, i) :
            sieve[j] = False

# 입력된 범위 내의 소수 개수를 찾기
def checkValue(value) :
    count = 0
    for i in range(value+1, value*2 + 1) : # n < x <= 2n
        if sieve[i] :
            count += 1
    return count

# 출력하기
while True :
    n = int(sys.stdin.readline().rstrip())
    if n == 0 :
        break
    elif n == 1 :
        print(1)
    else :
        result = checkValue(n)
        print(result)

# timeout
# while True :
#     n = map(int,sys.stdin.readline())
#     resultSet = {x for x in range(n, n*2+1)}
#     if n == 0 :
#         break
#     else :
#         for i in range(2, int((n*2)**0.5)+1) :
#             for j in range(i+i, n*2+1, i) :
#                 resultSet.discard(j)
#         if n == 1 :
#             resultSet.remove(1)
#         # print(resultSet)
#         print(len(resultSet))
