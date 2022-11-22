# https://www.acmicpc.net/problem/1874
import sys
try :
    N = int(input())
    answer = [int(sys.stdin.readline()) for _ in range(N)] # determined. ex) answer = [4,3,6,8,7,5,2,1]
    stack = [] # save numbers in asc (from 1 to N)
    lg = [] # log. Put one to stack, save '+' in li. Pop one from stack, save '-' in li.

    j = 0 # answer index
    for i in range(1,N+1) :
        stack.append(i) # stack = [1,2,3,...,N+1]
        lg.append('+') # log

        while j < N and answer[j] == stack[-1] : # jth answer value [4,3,6,8,7,5,2,1] matches last stack input [1,2,3,...,N+1]
            stack.pop() # pop one
            lg.append('-') # log
            j += 1 # next val
            if not stack:
                break
    
    if stack:
        print('NO')
    else :
        for char in lg :
            print(char)

except ValueError :
    print('Input Error')