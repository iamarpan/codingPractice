def catalan(n):
    n =2*n
    k=n
    res = 1
    if(k<n-k):
        k = n-k
    for a in range(k):
        res = res*(n-a)
        res = res/(n+a)
    return res

if __name__ == '__main__':
    n = int(input())
    print(catalan(n))
