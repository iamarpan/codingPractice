def lcs(a,b):
    if(len(a)==0 or len(b)==0):
        return 0
    elif(a[-1]==b[-1]):
        return 1+lcs(a[:-1],b[:-1])
    else:
        return max(lcs(a,b[:-1]),lcs(a[:-1],b))


def DPlcs(a,b):
    c = [[-1 for i in range(len(b)+1)] for j in range(len(a)+1)]
    a = ' ' + a
    b = ' ' + b
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==' ' or b[j]==' '):
                c[i][j]=0
            elif(a[i]==b[j]):
                c[i][j]=1+c[i-1][j-1]
            else:
                c[i][j]= max(c[i-1][j],c[i][j-1])
    return c[-1][-1]

if __name__ == '__main__':
    a = input("Enter string 1")
    b = input("Enter string 2")
    print(DPlcs(a,b))

