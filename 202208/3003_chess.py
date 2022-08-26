chessPieces = [1,1,2,2,2,8]
donghyukPieces = list(map(int, input().split()))
result = []
for i in range(6) :
    if chessPieces[i] == donghyukPieces[i] :
        result.append(0)
    else :
        gap = chessPieces[i] - donghyukPieces[i]
        result.append(gap)
        
print(*result)