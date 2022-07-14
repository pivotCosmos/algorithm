li = []
for i in range(9):
    li.append(int(input()))
n = max(li)
w = li.index(n)
print(n, w+1, sep='\n')