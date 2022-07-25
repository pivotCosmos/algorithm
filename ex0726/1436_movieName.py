n = int(input())
templi = []
m = 666
while True :
    strli = list(str(m))
    for i in range(len(strli)-2) :
        if strli[i] == '6' and strli[i+1] == '6' and strli[i+2] == '6' and m not in templi:
            templi.append(m)
    m += 1
    if len(templi) == n :
        break
print(templi[n-1])