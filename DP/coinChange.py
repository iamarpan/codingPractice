def coinChange(amount,coins):
    coins.insert(0,0)
    c = [[0 for a in range(amount+1)] for b in range(len(coins))]
    for i in range(len(coins)):
        for j in range(amount+1):
            if(j==0):
                c[i][j]=1
            elif(i==0):
                c[i][j]=0
            else:
                if(j-coins[i]>=0):
                    c[i][j]= c[i-1][j] + c[i][j-coins[i]]
                else:
                    c[i][j] =c[i-1][j]
    return c[len(coins)-1][amount]

if __name__ == '__main__':
    n = int(input("Enter amount"))
    coins = [int(a) for a in input().split()]
    print(coinChange(n,coins))
