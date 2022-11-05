import sys
# 스택
class stack():
    stack_list = []
    def stack_push(self,data) :
        self.stack_list.append(data)
    def stack_pop(self) :
        if self.is_empty() < 1 : # 비어있지 않다.
            value = self.stack_list.pop()
            return value
        else :
            return -1
    def stack_size(self) :
        size =  len(self.stack_list)
        return size
    def is_empty(self) :
        if self.stack_size() < 1 : # 비어있다
            return 1
        else : # 비어있지 않다
            return 0
    def stack_top(self) :
        if self.is_empty() < 1 : # 비어있지 않다
            top = self.stack_list[-1]
            return top
        else : # 비어있다
            return -1
        
N = int(input())
my_stack = stack()

for _ in range(N) :
    input_str = list(sys.stdin.readline().rstrip().split())
    command = input_str[0]
    if command == 'push' :
        value = int(input_str[1])
        my_stack.stack_push(value)
    elif command == 'pop' :
        print(my_stack.stack_pop())
    elif command == 'size' :
        print(my_stack.stack_size())
    elif command == 'empty' :
        print(my_stack.is_empty())
    elif command == 'top' :
        print(my_stack.stack_top())