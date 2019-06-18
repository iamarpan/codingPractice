def printBinary(digits, prefix=""):
    """ This function will take as input 
        number of digits of binary number 
        you want to print. e.g. 
        Input:2
        output:
        00
        01
        10
        11
    """    
    if(digits ==0):
        print(prefix)
    else:
        printBinary(digits-1,prefix+"0")
        printBinary(digits-1,prefix+"1")

if __name__ == '__main__':
    number = int(input("Enter number:\n"))
    printBinary(number)
