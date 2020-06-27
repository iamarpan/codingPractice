def partition(array,start,end):
    pivot = array[end]
    pIndex = start
    for i in range(start,end):
        if(array[i]<pivot):
            k = array[i]
            array[i] = array[pIndex]
            array[pIndex] = k
            pIndex+=1
    k = array[end]
    array[end] = array[pIndex]
    array[pIndex] = k
    return pIndex

def quickSort(array,start,end):
    if(start>=end):
        return
    pIndex = partition(array,start,end)
    quickSort(array,start,pIndex-1)
    quickSort(array,pIndex+1,end)



if __name__ == '__main__':
    array = list(map(int,input().split()))
    quickSort(array,0,len(array)-1)
    print(array)
