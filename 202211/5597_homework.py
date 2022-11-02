import sys
student_li = [x for x in range(1,31)]
for _ in range(28) :
    N = int(sys.stdin.readline())
    student_li.remove(N)
print(*student_li)