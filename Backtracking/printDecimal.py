import sys

def printDecimal(digits, prefix=""):
    """ This method will take as input 
    number of digits and output all decimal
    numbers containg that digits
    e.g. Input:1
    Output:
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """
    if(digits==0):
        print(prefix)
    else:
        for i in range(10):
            printDecimal(digits -1, prefix +str(i))

if __name__ == '__main__':
    try:
        number = int(input("enter number:\n"))
    except:
        sys.exit("Enter a valid value")
    printDecimal(number)
