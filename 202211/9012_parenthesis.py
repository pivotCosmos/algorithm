import sys
# 스택 구현
class stack :
    def __init__(self) :
        self.items = []
    def put(self,item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def is_empty(self) :
        return not self.items

N = int(input()) # 테스트 개수 입력
for _ in range(N) :
    half = stack()
    the_other_half = stack()
    input_values = list(sys.stdin.readline().rstrip())
    if len(input_values)%2 > 0 :
        print('NO')
    else :
        # 반만 그대로 꺼내서 스택에 쌓고, 다른 반은 반대 괄호를 다른 스택에 쌓는다.
        half_len = N//2
        for i in range(len(input_values)) :
            value = input_values[i]
            if i < half_len :
                half.put(value)
            else :
                reverse_value = ''
                if value == '(' :
                    reverse_value = ')'
                else :
                    reverse_value = '('
                the_other_half.put(reverse_value)
        # 스택에 저장된 데이터가 같으면 YES 아니면 NO
        for i in range(half_len) :
            if half.pop() != the_other_half.pop() : # 'stack' object is not subscriptable
                print('NO')
        print('YES')