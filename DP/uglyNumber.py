def ugly(n):
    ugly = []
    ugly.append(1)
    i2=i3=i5=0
    for a in range(1,n):
        next_multiple_2 = ugly[i2]*2
        next_multiple_3 = ugly[i3]*3
        next_multiple_5 = ugly[i5]*5
        ugly_no = min(next_multiple_2,next_multiple_3,next_multiple_5)
        ugly.append(ugly_no)
        if(ugly_no == next_multiple_2):
            i2+=1
        if(ugly_no == next_multiple_3):
            i3+=1
        if(ugly_no == next_multiple_5):
            i5+=1
    return ugly[-1]

if __name__ == '__main__':
    n = int(input("enter number for ugly number"))
    print(ugly(n))
