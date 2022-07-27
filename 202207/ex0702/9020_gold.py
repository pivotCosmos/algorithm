from itertools import *

# 에라토스테네스의 체
sieve = [x for x in range(2, 10000)]
for i in range(2, int(10000*0.5)) :
    for j in range(i*2, 10000, i) :
        if j in sieve :
            sieve.remove(j)

def find(x) :
    results = []
    sums = []
    for i in range(len(sieve)) :
        while x < sieve[i] :
            for j in range(len(sieve)) :
                while x < sieve[j] :
                    if sieve[i] + sieve[j] == x :
                        results.append([sieve[i], sieve[j]])
                        sums.append(sieve[i]+sieve[j])
    temp = min(sums)
    return results[temp]

T = int(input())
results = []
for i in range(T) :
    n = int(input())
    answer = find(n)
    print(*answer)