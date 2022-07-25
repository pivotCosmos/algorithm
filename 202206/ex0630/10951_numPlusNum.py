import sys
while True :
    try :
        n, m = map(int, sys.stdin.readline().split())
        print(n+m)
    except ValueError :
        break

# lines = sys.stdin.readlines()
# for line in lines :
#     n, m = map(int, line.split())
#     print(n+m)