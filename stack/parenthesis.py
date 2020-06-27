from collections import deque

def isBalanced(string):
    stack = deque()
    opening = ['(','{','[']
    closing = [')','}',']']
    pair = {'}':'{',')':'(',']':'['}
    for a in string:
        if a in opening:
            stack.append(a)
        else:
            if(len(stack)==0):
                return False
            elif((a=='}' and stack[-1]=='{') or (a==')' and stack[-1]=='(') or (a==']' and stack[-1]=='[')):
                stack.pop()
    if(len(stack)==0):
        return True
    else:
        return False

if __name__ == '__main__':
    n = input("enter string")
    tick = time.time()
    print(isBalanced(n))
    tock= time.time()
    print("time taken",tock-tick)
