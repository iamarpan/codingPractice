from collections import deque

if __name__ == '__main__':
    stack = deque()
    stack.append(5)
    stack.append(4)
    stack.append(3)
    stack.pop()
    stack.pop()
    print(stack)
