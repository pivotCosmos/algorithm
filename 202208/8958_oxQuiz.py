import sys

N = int(input())
ox_lists = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

for i in range (N) :
    total_score = 0
    ox_list = ox_lists[i]
    scores = []
    score_temp = 0
    for ox_pick in ox_list :
        if ox_pick == 'O' :
            score_temp += 1
        else :
            score_temp = 0
        scores.append(score_temp)
    print(sum(scores))