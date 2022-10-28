N,M = map(int,input().split())

def repeat(depth, max_num, result_li) :
    result_li_copy = result_li.copy()
    depth_copy = depth
    for j in range(1,max_num) :
        result_li_copy.append(j)
        depth_copy -= 1
        if depth_copy > 0 :
            repeat(depth_copy,max_num,result_li_copy)
        else :
            print(*result_li_copy)
        result_li_copy = result_li.copy()
        depth_copy = depth
            
results = []
repeat(M,N+1,results)