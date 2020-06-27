def permutation(n,k):
    c = [[0 for b in range(k+1)] for a in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if(j==0):
                c[i][j]=1
            else:
                c[i][j] = c[i-1][j] + j*c[i-1][j-1]
    return c[n][k]

if __name__ == '__main__':
    n = int(input("enter n : "))
    k = int(input("enter k: "))
    print(permutation(n,k))

