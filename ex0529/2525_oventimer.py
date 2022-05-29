h,m=map(int, input().split())
cookingtime = int(input())

if((m+cookingtime)>=60) :
    temp = (m+cookingtime)//60
    m = (m+cookingtime)%60
    if((h+temp)>=24) :
        h = h+temp-24
    else :
        h = h+temp
else :
    m = m+cookingtime

print(h,m)