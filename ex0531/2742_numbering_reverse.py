n = int(input())
temp = []
while n >= 1 :
    temp.append(n)
    n = n - 1
print(*temp, sep="\n")