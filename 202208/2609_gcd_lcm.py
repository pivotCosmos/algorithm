# 최대공약수, 최소공배수 구하기
N, M = map(int, input().split())

def get_submultiples(number) :
    submultiples_of_number = []
    for i in range(2, int(number/2)) :
        if number%i == 0 :
            submultiples_of_number.append(i)
    submultiples_of_number.sort(reverse=True)
    return submultiples_of_number

def get_GCD(num1, num2) :
    GCD = 0
    submultiples_num1 = get_submultiples(num1)
    submultiples_num2 = get_submultiples(num2)
    smaller_list = []

    if N < M :
        smaller_list = submultiples_num1
    else :
        smaller_list = submultiples_num2

    for s in smaller_list :
        if s in smaller_list :
            GCD = s
            break
    return GCD

print(get_GCD(N,M))