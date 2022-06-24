w = int(input())

result = -1
for i in range (0,w//5+1) :
    f = w//5 -i
    t = (w%5 + 5*i)//3
    if (w%5 + 5*i)%3 == 0 :
        result = f+t
        break
print(result)