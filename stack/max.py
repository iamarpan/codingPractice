class Stack:
    def __init__(self):
        self.top = -1
        self.size=10
        self.stack=[None]*self.size

    def push(self,value):
        if(self.isFull()):
            print("stack is full")
        else:
            if(self.isEmpty()):
                self.top+=1
                self.stack[self.top]=(value,value)
            else:
                maximum = max(value,self.stack[self.top][1])
                self.top+=1
                self.stack[self.top]= (value,maximum)

    def pop(self):
        if(self.isEmpty()):
            print("stack is empty")
        else:
            self.top-=1

    def max(self):
        return self.stack[self.top][1]

    def isEmpty(self):
        if(self.top==-1):
            return True
        return False

    def isFull(self):
        if(self.top==self.size):
            return True

    def print(self):
        while(not self.isEmpty()):
            print(self.stack[self.top])


if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    print("max",stack.max())
    stack.push(3)
    print("max",stack.max())
    stack.push(4)
    stack.push(5)
    print("max",stack.max())
    stack.push(1)
    print("max",stack.max())
    stack.pop()
    print("max",stack.max())
    stack.pop()
    print("max",stack.max())
    stack.pop()
    print("max",stack.max())
