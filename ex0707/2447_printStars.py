def printStars (l,n) :
    if n == l :
        return
    elif l == 0 :
        print('***'*n)
        print('* *'*n)
        print('***'*n)
        printStars(l+1, n)
    elif l == 1 :
        print('***   ***')
        print('* *   ***')
        print('***   ***')
        printStars(l+1, n)
    elif l == 2 :
        print('***'*n)
        print('* *'*n)
        print('***'*n)
        printStars(l+1, n)

printStars(0,int(input()))