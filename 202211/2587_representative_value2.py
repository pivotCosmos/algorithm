numbers= []
for _ in range(5) :
    numbers.append(int(input()))
numbers.sort()
avg = sum(numbers)//5
center = numbers[2]
print(avg,center,sep='\n')