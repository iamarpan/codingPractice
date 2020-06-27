def goldmine(c):
    X = [[c[i][j] for i in range(len(c))] for j in range(len(c[0]))]
    minimum = -1
    count = max((X[0]))
    left =-1
    right=-1
    initialj = X[0].index(count)
    for a in range(1,len(X)):
        if(initialj>0):
            left = initialj-1
        if(initialj<len(X[0])-1):
            right = initialj+1
        mid = initialj
        value=max(X[a][left],X[a][right],X[a][mid])
        count+=value
        initialj = X[a].index(value)
    return count

if __name__ == '__main__':
    c = [[10,33,13,15],[22,21,4,1],[5,0,2,3],[0,6,14,2]]
    print(goldmine(c))
        


        
