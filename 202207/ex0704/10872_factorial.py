# # for문
# n = int(input())
# result = 1
# if n == 0 :
#     result = 1
# else :
#     while n > 0 :
#         result = result * n
#         n = n - 1
# print(result)

# 재귀
def factorial(n) :
    if n==0 or n == 1:
        return 1
    else :
        return n*factorial(n-1)

print(factorial(int(input())))