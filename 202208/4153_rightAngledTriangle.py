import sys
while True :
    sides = list(map(int, sys.stdin.readline().split()))
    if sides == [0,0,0] :
        break
    else :
        m = max(sides)
        squares = [i * i for i in sides if i != m]
        if m**2 == sum(squares) :
            print("right")
        else :
            print("wrong")