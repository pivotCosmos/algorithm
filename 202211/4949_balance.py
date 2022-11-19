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
        break
    my_stack = stack()
    result = 'yes'
    for letter in line :
        if letter == '(' or letter == '[':
            my_stack.push(letter)
        elif letter == ')' or letter == ']':
            if my_stack.is_empty() :
                result = 'no'
                break
            else :
                stack_value = my_stack.pop()
                if stack_value == '(' :
                    if letter == ']' :
                        result = 'no'
                        break
                elif stack_value == '[' :
                    if letter == ')' :
                        result = 'no'
                        break
    if not my_stack.is_empty():
        result = 'no'
    print(result)