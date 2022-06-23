import sys, math
testNum = int(input())
for i in range(testNum) :
    h,w,n = map(int, sys.stdin.readline().split())
    if n%h ==0 :
        hId = h
    else :
        hId = n%h
    # wId = format(math.ceil(n/h), '02')
    wId = str(math.ceil(n/h)).zfill(2)
    print(hId,wId,sep='')
