N = int(input())
def factorial(inputNum) :
    num = inputNum
    result = 1
    while num>1 :
        result *= num
        num -= 1
    return result

# 뒤에서부터 연속된 0의 개수 출력
facResult = factorial(N)
facString = str(facResult)
facList = list(facString)
result = 0
if facResult < 10 :
    print(0)
else :
    for i in range(1, len(facList)) :
        if int(facList[-i]) == 0 :
            result += 1
        else :
            print(result)
            break