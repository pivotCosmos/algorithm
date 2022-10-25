N,M = map(int, input().split())
original_li = [x for x in range(1,N+1)]
# 두개 뽑는다고 가정
for i in original_li :
    copy_list = original_li.copy() # 깊은 복사
    one = i
    copy_list.remove(one)
    for j in copy_list :
        result_li = [one]
        result_li.append(j)
        print(*result_li)