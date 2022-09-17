# 최대공약수, 최소공배수 구하기
N, M = map(int, input().split())

GCD = 0
LCM = 0

def get_submultiples(number) :
    submultiples_of_number = []
    for i in range(number/2) :
        if number%i == 0 :
            submultiples_of_number.append(i)
    submultiples_of_number.sort(reverse=True)
    return submultiples_of_number

submultiples_of_N = get_submultiples(N)
submultiples_of_M = get_submultiples(M)

smaller_list = []

if N < M :
    smaller_list = submultiples_of_N
else :
    smaller_list = submultiples_of_M

for s in smaller_list :
    if s in smaller_list :
        GCD = s
        break

