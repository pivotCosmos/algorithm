import math, sys
n,m = map(int, sys.stdin.readline().split())
c = math.comb(n,m)
r = 0
while c > 10 :
    left = c%10
    if left==0 :
        r += 1
        c //= 10
    else :
        break
print(r)