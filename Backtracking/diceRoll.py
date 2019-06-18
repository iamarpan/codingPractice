def diceRoll(digits,prefix=""):
    """This function will take the number of 
        dices you want to roll and output all
        the possible combinations.
    """

    if(digits ==0):
        value = " ".join(prefix.split(",")).split()
        print(value)
    else:
        for a in range(1,7):
            diceRoll(digits-1,prefix+str(a)+',')


if __name__ == '__main__':
    try:
       number =  int(input("Enter number of dices:\n"))
    except:
        sys.exit("Enter valid number of digits")
    diceRoll(number)
