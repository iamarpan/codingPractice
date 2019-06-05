def SelectionSort(arrayList):
    for i in range(len(arrayList)):
        iMin = i
        for j in range(i+1,len(arrayList)):
            if(arrayList[iMin]>arrayList[j]):
                iMin = j
        temp = arrayList[iMin]
        arrayList[iMin] = arrayList[i]
        arrayList[i] = temp

    print(arrayList)

if __name__ == '__main__':
    arrayList = [int(a) for a in input("enter space separated values:\n").split()]
    try:
        SelectionSort(arrayList)
    except:
        raise Exception("No. of elements should be more than 1")


