n = int(input())
m = 0 # 팩토리얼
k = 0 
val = 0 # 몇번째 순서
for  i in range(1, n+1) :
    m = m + i
    val = val + 1
    if m >= n :
        k = m - n
        break
#print(f"val : {val} , m = {m}, k = {k}")

li=[]
if val%2 == 0 : #짝수 번째 순서이면
    li = [val-k, 1+k]
else :
    li = [1+k, val-k]
print(*li, sep='/')