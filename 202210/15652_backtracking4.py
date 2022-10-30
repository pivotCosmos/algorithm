N,M = map(int,input().split())

def repeat(depth, max_num, result_li, now_value) :
    result_li_copy = result_li.copy()
    depth_copy = depth
    for j in range(now_value,max_num) :
        result_li_copy.append(j)
        depth_copy -= 1
        if depth_copy > 0:
            now_value = j
            repeat(depth_copy,max_num,result_li_copy,now_value)
        else :
            print(*result_li_copy)
        result_li_copy = result_li.copy()
        depth_copy = depth
            
results = []
repeat(M,N+1,results,1)