from collections import Counter
import math

n = int(input())
li = []
for i in range(n) :
    li.append(int(input()))
re = []

# 산술평균
a = round(sum(li)/n)
re.append(a)

# 중앙값
new_li = sorted(li)
i = int((n/2)-0.5)
re.append(new_li[i])

# 최빈값
counter_li = Counter(li)
order_li = counter_li.most_common()
temp = []

for num in order_li :
    if num[1] == order_li[0][1] :
        temp.append(num[0])

if len(temp) > 1 :
    re.append(sorted(temp)[1])
else :
    re.append(temp[0])

# 범위
r = max(li) - min(li)
re.append(r)

print(*re, sep='\n')