import sys

# 에라토스테네스의 체
sieve = [x for x in range(2, 10001)]
for i in range(2, int(10000*0.5)+1) :
    for j in range(i*2, 10001, i) :
        if j in sieve :
            sieve.remove(j)

def find(x) :
    one = 0; two = 10001
    for i in range(len(sieve)) :
        v = x - sieve[i]
        if v in sieve :
            if v >= sieve[i] : # one <= two
                one = sieve[i]
                two = v
            else :
                break
    return one, two

T = int(sys.stdin.readline())
for _ in range(T) :
    n = int(sys.stdin.readline())
    answer = find(n)
    print(*answer)