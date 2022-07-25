# v = 올라갈 높이, a = 1일 등반 높이, b = 1일 미끄러지는 높이
a,b,v = list(map(int,input().split()))
v = v-a # 마지막날에 올라가는 것 먼저 뺀다
temp = 1
if v%(a-b) ==0 :
    temp = temp + v//(a-b)
else :
    temp = temp + v//(a-b) +1
print(temp)