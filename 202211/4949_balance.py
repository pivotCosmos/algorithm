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

while True :
    line = list(sys.stdin.readline().rstrip())
    if line == ['.'] :
        break # while문 탈출
    my_stack_round = stack()
    my_stack_square = stack()
    result = 'YES'
    for letter in line :
        if letter == '(':
            my_stack_round.push(letter)
        elif letter == ')':
            if my_stack_round.is_empty() :
                result = 'NO'
                break
            my_stack_round.pop()
        elif letter == '[':
            my_stack_square.push(letter)
        elif letter == ']':
            if my_stack_square.is_empty() :
                result = 'NO'
                break
            my_stack_square.pop()
    if not my_stack_round.is_empty() or not my_stack_square.is_empty():
        result = 'NO'
    print(result)