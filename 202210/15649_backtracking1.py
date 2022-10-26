N,M = map(int, input().split())
original_li = [x for x in range(1,N+1)]
result_li = []

def get_new_result_li(copy_li, result_li, total_pick) :
    if total_pick > 0 :
        for i in copy_li :
            new_result_li = result_li.copy()
            pick = i
            new_result_li.append(pick)

            new_copy_li = copy_li.copy()
            new_copy_li.remove(pick)
            get_new_result_li(new_copy_li,new_result_li,total_pick-1)
    else :
        print(*result_li)
    return 0

get_new_result_li(original_li, result_li, M)