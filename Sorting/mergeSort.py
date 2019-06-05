def Merge(left, right, arrayList):
    lengthOfLeft = len(left)
    lengthOfRight = len(right)
    n =len(arrayList)
    i=0
    j=0
    k=0
    while(i<lengthOfLeft and j<lengthOfRight):
        if(left[i]>right[j]):
            arrayList[k]= left[i]
            i+=1
        else:
            arrayList[k] = right[j] 
            j+=1
        k+=1
    while(i<lengthOfLeft):
        arrayList[k]= left[i]
        k+=1
        i+=1
    while(j<lengthOfRight):
        arrayList[k]= right[j]
        k+=1
        j+=1


def MergeSort(arrayList):
    n = len(arrayList)
    if(n<2):
        return
    mid = n//2
    left = arrayList[0:mid]
    right = arrayList[mid:len(arrayList)]
    MergeSort(left)
    MergeSort(right)
    Merge(left, right, arrayList)
    return arrayList


if __name__ == '__main__':
    arrayList = [int(a) for a in input("enter space separated values:\n").split()]
    array = MergeSort(arrayList)
    print(array)
