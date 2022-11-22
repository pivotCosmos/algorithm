import sys
# stack
class stack :
    def __init__(self) :
        self.items = []
    def push(self, item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def is_empty(self) :
        return not self.items

N = int(input())
# setting
my_stack = stack()
my_list = []
for _ in range(N) :
    num = int(sys.stdin.readline())
    my_stack.push(num)
    my_list.append(num)
now_value = 0
count = 0 # 오름차순 수열의 수 개수
result_li = []
# check if the numbers are descending after the max value
max_index = my_list.index(N)
my_list_sliced = my_list[max_index:len(my_list)]
my_list_sliced_dsc = sorted(my_list_sliced,reverse=True)
if my_list_sliced != my_list_sliced_dsc :
    print('NO')
else :
    #print
    while not my_stack.is_empty() :
        now_value += 1
        stack_value = my_stack.pop()
        if now_value == stack_value :
            result_li.append('+')
            count += 1
        elif now_value < stack_value :
            gap = stack_value - now_value
            result_li += ['+']*gap
            result_li += ['-']*gap
            result_li.append('+')
            now_value += gap
            count += 1
        else :
            result_li += ['-']*count
            break
    print(*result_li,sep="\n")