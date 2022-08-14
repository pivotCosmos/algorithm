import sys
points = [list(map(int, sys.stdin.readline().split())) for i in range(3)]
result = []

points.sort()

if points[0][0] != points[1][0] :
    result.append(points[0][0])
elif points[-1][0] != points[-2][0] :
    result.append(points[-1][0])

points.sort(key=lambda x : x[1])

if points[0][1] != points[1][1] :
    result.append(points[0][1])
elif points[-1][1] != points[-2][1] :
    result.append(points[-1][1])

print(*result)