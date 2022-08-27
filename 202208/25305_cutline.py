import sys
candidate_number, winner_number = map(int, input().split())
scores = list(map(int,sys.stdin.readline().split()))
scores.sort(reverse=True)
MIN_INDEX = winner_number - 1
MIN_SCORE = scores[MIN_INDEX]
print(MIN_SCORE)