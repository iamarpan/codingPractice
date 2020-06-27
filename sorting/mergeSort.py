def merge(A,B):
    C = []
    while(len(A)>0 and len(B)>0):
        if(A[0]<B[0]):
            C.append(A[0])
            A = A[1:]
        else:
            C.append(B[0])
            B = B[1:]
    if(len(A)>0):
        C+=A
    if(len(B)>0):
        C+=B
    return C

def mergeSort(a,n):
    if(n==1):
        return a
    m = n//2
    A = mergeSort(a[:m],len(a[:m]))
    B = mergeSort(a[m:],len(a[m:]))
    c = merge(A,B)
    return c

if __name__ == "__main__":
    array = list(map(int,input().split()))
    print(mergeSort(array,len(array)))
