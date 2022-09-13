# 배수와 약수
import sys

input_numbers = []
while True :
    input_numbers = list(map(int, sys.stdin.readline().split()))
    if input_numbers == [0,0] :
        break
    else :
        first_num = input_numbers[0]
        second_num = input_numbers[1]
        #if second_num > first_num : # 유의미한 시간 차이 없음
        if second_num % first_num == 0 :
            print("factor")
        elif first_num % second_num == 0 :
            print("multiple")
        else :
            print("neither")