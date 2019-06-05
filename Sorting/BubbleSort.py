def BubbleSort(arrayList):
    n=len(arrayList)

    for a in range(len(arrayList)):
        flag = 0
        for b in range(n-a-1):
            if(arrayList[b]>arrayList[b+1]):
                temp = arrayList[b]
                arrayList[b] = arrayList[b+1]
                arrayList[b+1] = temp
                flag= 1
        if(flag==0):
            break
   
    print(arrayList)


if __name__ == '__main__':
    arrayList = [int(a) for a in input("Enter space separated values as input").split(" ")]
    BubbleSort(arrayList)
