# # 방정식으로 풀기
# from sympy import Symbol, solve

# #고정비용, 생산비용, 노트북가격
# A,B,C = map(int, input().split())

# x = Symbol('x')
# equation = A + B*x -C*x;
# solve(equation)


# # while문으로 풀기(시간초과)
# A,B,C = map(int, input().split())
# x = 0
# if B>=C:
#     print(-1)
# else :
#     while A + B*x -C*x > 0 :
#         x = x + 1
#     print(x+1)


# # 틀린 예시
# import math
# A,B,C = map(int, input().split())
# if B>=C:
#     print(-1)
# else :
#     x = math.ceil(A/(C-B)) # ceil하면 +1효과가 나서 안됨
#     print(x+1)


A,B,C = map(int, input().split())
if B>=C:
    print(-1)
else :
    x = (A//(C-B))
    print(x+1)