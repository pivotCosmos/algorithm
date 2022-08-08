import sys
N = int(input())
words = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
words = set(words) # set자료형으로 변환해서 중복제거
newWords = sorted(words, key=lambda x : (len(x),x))
print(*newWords,sep='\n')