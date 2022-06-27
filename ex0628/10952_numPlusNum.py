import sys
for line in sys.stdin :
    n, m = map(int, line.split())
    if n == 0 and m == 0 :
        break
    print(n + m)