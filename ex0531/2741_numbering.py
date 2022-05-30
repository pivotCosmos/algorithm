n = int(input())
i = 1
temp = []
while i <= n :
    temp.append(i)
    i = i + 1
print(*temp, sep="\n")