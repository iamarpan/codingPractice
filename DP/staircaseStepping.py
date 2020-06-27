def step(steps,memo):
    if(steps<0):
        return 0
    if(steps==0):
        return 1
    else:
        return step(steps-1)+step(steps-2)

def bottomUp(steps):
    i=0
    j=1
    for a in range(2,steps+2):
        k = i+j
        i=j
        j=k
    return k
    
if __name__ == '__main__':
    n = int(input("Enter stair size"))
    print(bottomUp(n))
