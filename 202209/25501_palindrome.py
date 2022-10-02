import sys

def recursion(str,start,end, count) :
    if(start >= end) :
        return [1,count]
    elif str[start] != str[end] :
        return [0,count]
    else :
        return recursion(str, start+1, end-1, count+1)

def isPalindrome(str) :
    results = recursion(str, 0 , len(str)-1, 1)
    return results

N = int(sys.stdin.readline())
str_li = []
for _ in range(N) :
    str = list(sys.stdin.readline().rstrip())
    results = isPalindrome(str)
    print(*results, sep=' ')