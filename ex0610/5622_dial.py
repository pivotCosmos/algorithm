n = list(input())
time = 0
for i in range(len(n)) :
    #print(n[i])
    #print(ord(n[i]))
    if ord(n[i]) <= ord('C'):
        time = time + 3
    elif ord(n[i]) <= ord('F'):
        time = time + 4
    elif ord(n[i]) <= ord('I'):
        time = time + 5
    elif ord(n[i]) <= ord('L'):
        time = time + 6
    elif ord(n[i]) <= ord('O'):
        time = time + 7
    elif ord(n[i]) <= ord('S'):
        time = time + 8
    elif ord(n[i]) <= ord('V'):
        time = time + 9
    elif ord(n[i]) <= ord('Z'):
        time = time + 10
print(time)