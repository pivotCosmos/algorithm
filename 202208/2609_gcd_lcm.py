# 최대공약수, 최소공배수 구하기
N, M = map(int, input().split())

def sort_inputs_asc(N, M) :
    small_num = N if N < M else M
    big_num = N if N > M else M
    results = [small_num, big_num]
    return results

def get_submultiples(number) :
    submultiples = []
    for i in range(2, int(number/2)) :
        if number%i == 0 :
            submultiples.append(i)
    submultiples.sort(reverse=True)
    return submultiples

def get_GCD(num1, num2) :
    GCD = 0
    nums = sort_inputs_asc(num1, num2)
    small_submultiples = get_submultiples(nums[0])
    big_submultiples = get_submultiples(nums[1])

    for big_submultiple in big_submultiples :
        if big_submultiple in small_submultiples :
            GCD = big_submultiple
            break
    return GCD

print(get_GCD(N,M))