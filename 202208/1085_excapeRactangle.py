x, y, w, h = map(int, input().split())

def getTheShortestDistance (x, y, w, h):
    gaps = [x, y] # x축, y축과의 거리
    upDownGap = x - w
    leftRightGap = y - h
    
    gaps.append(upDownGap)
    gaps.append(leftRightGap)
    
    temp = []
    for i in range(len(gaps)) :
        temp.append(gaps[i]**2)
    
    index = temp.index(min(temp))
    choice = gaps[index]

    if choice < 0 :
        choice = choice*(-1)
    return choice

print(getTheShortestDistance(x, y, w, h))