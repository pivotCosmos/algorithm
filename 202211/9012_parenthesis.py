import sys
# 스택 구현
class stack :
    def __init__(self) :
        self.items = []
    def push(self,item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def is_empty(self) :
        return not self.items

N = int(input()) # 테스트 개수 입력
for _ in range(N) :
    line_list = list(sys.stdin.readline().rstrip())
    my_stack = stack()
    result = ''
    for one in line_list :
        if one == '(' :
            my_stack.push(one)
        else :
            if my_stack.is_empty() : # '('이 부족
                result = 'NO'
                break
            else :
                my_stack.pop()
    if result == 'NO' :
        print(result)
    else :
        if my_stack.is_empty() :
            print('YES')
        else :
            print('NO') # '('이 남음