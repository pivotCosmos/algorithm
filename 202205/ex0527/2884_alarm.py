h,m = map(int, input().split())
if m >= 45:
    print(h, m-45)
elif m < 45:
    if h >= 1:
        print(h-1, m+60-45)
    elif h ==0:
        print(23, m+60-45)