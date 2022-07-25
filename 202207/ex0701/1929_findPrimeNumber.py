# 에라토스테네스의 체
n,m = map(int, input().split())
primeNumbers = {x for x in range(n, m+1)}

for i in range(2, int(m**0.5)+1) :
    for j in range(i+i, m+1, i) :
        primeNumbers.discard(j)
if n == 1 :
    primeNumbers.remove(1)
mylist = list(primeNumbers)
mylist.sort()
print(*mylist, sep='\n')



# 시간초과
# n,m = map(int, input().split())
# primeNumbers = set(x for x in range(n, m+1))
# while m >= n :
#     for i in range(2, m) :
#         if m%i == 0 :
#             primeNumbers.remove(m)
#             break
#     m = m - 1
# if n == 1 :
#     primeNumbers.remove(1)
# print(*primeNumbers, sep='\n')