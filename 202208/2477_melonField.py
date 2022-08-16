K = int(input())
directions = []
widths = []
dtemp = []
wtemp = []
for i in range(6) :
    d, w = map(int, input().split())
    if directions.count(d) > 0 :
        index = directions.index(d)
        oldWidth = widths[index]
        dtemp.append(d)
        if w < oldWidth :
            wtemp.append(w)
        else :
            directions.remove(d)
            directions.append(d)
            widths[index] = w
            wtemp.append(oldWidth)
    else  :
        directions.append(d)
        widths.append(w)
print(f"directions = {directions}")
print(f"widths = {widths}")
print(f"dtemp = {dtemp}")
print(f"wtemp = {wtemp}")
templi = [x for x in directions if x not in dtemp]
bigSquare = widths[directions.index(templi[0])] * widths[directions.index(templi[1])]
smallSquare = wtemp[0] * wtemp[1]
# result = (bigSquare - smallSquare) * K
# print(result)
print(f"({bigSquare} - {smallSquare}) * {K} = {(bigSquare - smallSquare) * K}")