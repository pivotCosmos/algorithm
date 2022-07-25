import sys

h, w = map(int, input().split())
li = []
for i in range(h) :
    li.append(list(sys.stdin.readline()))

def paint(i,j,temp) :
    count = 0
    for k in range(8) :
        for l in range(8) :
            if (k%2 == 0 and l%2 == 0) or (k%2 != 0 and l%2 != 0) :
                if li[i+k][j+l] != temp :
                    count += 1
            else :
                if li[i+k][j+l] == temp :
                    count += 1
    return count

results = []
for i in range(h-7) :
    for j in range(w-7) :
        for str in ('B','W') :
            count = paint(i,j,str)
            results.append(count)
print(min(results))