def selectionSort(a):
    n = len(a)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if(a[minIndex]>a[j]):
                minIndex = j
        k = a[i]
        a[i] = a[minIndex]
        a[minIndex] = k
    return a

if __name__ == '__main__':
    a = list(map(int,input().split()))
    print(selectionSort(a))
