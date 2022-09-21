import sys

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

#GCD
def get_gcd(num1, num2) :
    while num2 != 0 :
        temp = num1
        num1 = num2
        num2 = temp%num1
    return num1

def get_gcd_of_list(list) :
    gcds = []
    for i in range(len(list)) :
        if i == 0 :
            temp_gcd = get_gcd(list[i],list[i+1])
        else :
            temp_gcd = get_gcd(temp_gcd, list[i])
        if temp_gcd != 1 :
            gcds.append(temp_gcd)
    return gcds

# 나머지가 같아지는 수
min_num = min(numbers)
gcds = []
for i in range(1, min_num) :
    new_numbers = [x-i for x in numbers]
    temp_gcds = get_gcd_of_list(new_numbers)
    gcds += temp_gcds
gcds_map = set(gcds)
gcds_list = list(gcds_map)
gcds_list.sort()
print(*gcds_list, sep="\n")