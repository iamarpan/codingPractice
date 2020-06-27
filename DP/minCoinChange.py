def coinChange(amount,coins):
    cache = [amount+1 for a in range(amount+1)]
    cache[0]=0
    for a in range(1,amount+1):
        for b in coins:
            if(a-b>=0):
                cache[a] = min(cache[a-b]+1,cache[a])
        if(cache[a]==amount+1):
            cache[a]=0
    print(cache)
    return cache[-1]

if __name__ == '__main__':
    amount = int(input())
    coins = [int(a) for a in input().split()]
    print(coinChange(amount,coins))

    
