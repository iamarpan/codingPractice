from collections import deque
def postfixEval(string):
    stack = deque()
    operator = ['*','+','-','/']
    for a in string:
        if a not in operator:
            stack.append(a)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            val = str(eval(op1 +a+ op2))
            stack.append(val)
    return stack.pop()

if __name__ == '__main__':
    n = input("enter string")
    print(postfixEval(n))

