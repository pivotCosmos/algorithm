def solution(lottos, win_nums):
    LEN_LOTTOS = 6
    check = 0
    lost = 0
    for i in range(LEN_LOTTOS) :
        my_num = lottos[i]
        if my_num > 0 :
            if my_num in win_nums :
                check += 1
        else :
            lost += 1
    min,max = 0,0
    if check == 6 :
        min = 1
    elif check == 5 :
        min = 2
    elif check == 4 :
        min = 3
    elif check == 3 :
        min = 4
    elif check == 2 :
        min = 5
    else :
        min = 6
    max = min - lost
    if max < 1 :
        max = 1
    answer = [max,min]
    return answer