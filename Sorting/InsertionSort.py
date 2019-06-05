def InsertionSort(arrayList):
    for i in range(1,len(arrayList)):
        value = arrayList[i]
        hole = i
        while(hole> 0 and arrayList[hole -1]>value):
            arrayList[hole] = arrayList[hole-1]
            hole = hole-1
        arrayList[hole]= value
    print(arrayList)


if __name__ == '__main__':
    arrayList = [int(a) for a in input("enter space separated values: \n").split()]
    InsertionSort(arrayList)
