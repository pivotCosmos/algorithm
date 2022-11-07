import sys
N= int(input())
class stack:
    def __init__(self) : # 생성될때 실행
        self.items = []
    def put(self,item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def is_empty(self) :
        return not self.items

my_stack = stack()
for _ in range(N):
    input_num = int(sys.stdin.readline())
    if input_num > 0 :
        my_stack.put(input_num)
    else :
        my_stack.pop()

stack_sum = 0
for _ in range(len(my_stack.items)) :
    stack_sum += my_stack.pop()
print(stack_sum)