nums = [int(input()) for _ in range(3)]
temp = nums[0]*nums[1]*nums[2]
tempstr = str(temp)
occurli = [0]*10
for i in tempstr :
    occurli[int(i)] += 1
print(*occurli,sep='\n')