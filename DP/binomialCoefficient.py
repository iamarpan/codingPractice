def coefficient(n,k):
    c = [[0 for b in range(k+1)] for a in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if(j==0 or i==j):
                c[i][j]=1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c[n][k]



if __name__ == '__main__':
    n = int(input("Enter n"))
    k = int(input("Enter k"))
    print(coefficient(n,k))
