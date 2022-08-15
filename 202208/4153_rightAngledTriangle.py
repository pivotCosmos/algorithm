import sys
while True :
    sides = list(map(int, sys.stdin.readline().split()))
    sides.sort()
    squares = [i * i for i in sides]
    if sides == [0,0,0] :
        break
    else :
        if squares[2] == (squares[1] + squares[0]) :
            print("right")
        else :
            print("wrong")